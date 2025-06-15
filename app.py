import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler
import os
from dotenv import load_dotenv
from styles import apply_custom_styles


load_dotenv()


st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)


apply_custom_styles()


st.markdown("""
<div class="main-header">
    <h1>🔍 AI Research Assistant</h1>

</div>
""", unsafe_allow_html=True)


with st.sidebar:
    st.markdown("###  Configuration")
    

    api_key = st.text_input(
        " Enter your Groq API Key:",
        type="password",
        help="Get your API key from https://console.groq.com/"
    )
    
    st.markdown("###  Search Sources")
    

    use_arxiv = st.checkbox(" arXiv (Academic Papers)", value=True)
    use_wikipedia = st.checkbox(" Wikipedia", value=True)
    use_web_search = st.checkbox(" Web Search", value=True)
    
    st.markdown("###  Model Settings")
    

    model_choice = st.selectbox(
        "Select Model:",
        ["Gemma2-9b-it", "llama3-8b-8192", "mixtral-8x7b-32768"],
        help="Choose the AI model for responses"
    )
    

    temperature = st.slider(
        "Response Creativity:",
        min_value=0.0,
        max_value=1.0,
        value=0.1,
        step=0.1,
        help="Lower values = more focused, Higher values = more creative"
    )


    if st.button(" Clear Chat History"):
        st.session_state["messages"] = []
        st.rerun()

@st.cache_resource
def initialize_tools():
    """Initialize and cache the research tools"""

    api_wrapper_arxiv = ArxivAPIWrapper(
        top_k_results=2,
        doc_content_chars_max=500
    )
    arxiv_tool = ArxivQueryRun(api_wrapper=api_wrapper_arxiv)
    

    api_wrapper_wiki = WikipediaAPIWrapper(
        top_k_results=2,
        doc_content_chars_max=500
    )
    wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper_wiki)
    

    search_tool = DuckDuckGoSearchRun(name="web_search")
    
    return arxiv_tool, wiki_tool, search_tool


col1, col2 = st.columns([3, 1])

with col1:

    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {
                "role": "assistant",
                "content": "Hello! I'm your AI Research Assistant. I can help you find accurate information from academic papers (arXiv), Wikipedia, and the web. What would you like to research today?"
            }
        ]
    

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
    

    if prompt := st.chat_input("Ask me anything... (e.g., 'Explain quantum computing applications')"):
        if not api_key:
            st.error(" Please enter your Groq API key in the sidebar to continue.")
            st.stop()
        

        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        llm = ChatGroq(
            model=model_choice,
            groq_api_key=api_key,
            streaming=True,
            temperature=temperature
        )


        arxiv_tool, wiki_tool, search_tool = initialize_tools()
        tools = []
        
        if use_arxiv:
            tools.append(arxiv_tool)
        if use_wikipedia:
            tools.append(wiki_tool)
        if use_web_search:
            tools.append(search_tool)
        
        if not tools:
            st.error(" Please select at least one search source in the sidebar.")
            st.stop()


        system_prompt = f"""You are a professional research assistant. Your goal is to provide accurate, detailed, and well-sourced information.

        Instructions:
        1. Always search for the most current and relevant information
        2. Provide specific details, not generic answers
        3. Include relevant examples, data, or statistics when available
        4. Cite your sources clearly
        5. If information is conflicting, mention different perspectives
        6. Structure your response clearly with main points
        7. Be comprehensive but concise

        User Query: {prompt}
        
        Please provide a detailed, accurate response using the available tools."""
        

        search_agent = initialize_agent(
            tools,
            llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            handling_parsing_errors=True,
            verbose=True,
            max_iterations=5,
            early_stopping_method="generate"
        )
        

        with st.chat_message("assistant"):
            with st.spinner("🔍 Searching for accurate information..."):
                st_cb = StreamlitCallbackHandler(
                    st.container(),
                    expand_new_thoughts=True,
                    collapse_completed_thoughts=True
                )
                
                try:

                    response = search_agent.run(system_prompt, callbacks=[st_cb])
                    st.session_state.messages.append({
                        'role': 'assistant',
                        "content": response
                    })
                    st.write(response)
                    
                except Exception as e:
                    error_msg = f"⚠️ An error occurred: {str(e)}"
                    st.error(error_msg)
                    st.session_state.messages.append({
                        'role': 'assistant',
                        "content": error_msg
                    })


with col2:
    st.markdown("###  Tips for Better Results")
    
    st.markdown("""
    <div class="info-box">
    <strong> Be Specific:</strong><br>
    Instead of "What is AI?", try "What are the latest applications of AI in healthcare?"
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <strong> Ask for Data:</strong><br>
    Request statistics, examples, or recent developments for more detailed answers.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <strong> Multiple Sources:</strong><br>
    Enable all search sources for comprehensive results.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("###  Recent Searches")
    if len(st.session_state.messages) > 1:
        user_messages = [msg for msg in st.session_state.messages if msg["role"] == "user"]
        for i, msg in enumerate(user_messages[-3:], 1):
            st.markdown(f"**{i}.** {msg['content'][:50]}...")
    else:
        st.markdown("*No recent searches*")


st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 1rem;'>
    Built with using Streamlit and LangChain | 
    <a href='https://console.groq.com/' target='_blank'>Get Groq API Key</a>
</div>
""", unsafe_allow_html=True)