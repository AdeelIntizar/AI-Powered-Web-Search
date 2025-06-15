import streamlit as st

def apply_custom_styles():
    """Apply custom CSS styles to the Streamlit app"""
    
    st.markdown("""
    <style>
        /* Main header styling */
        .main-header {
            text-align: center;
            padding: 2rem 0;
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 10px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .main-header h1 {
            margin: 0;
            font-size: 2.5rem;
            font-weight: bold;
        }
        
        .main-header p {
            margin: 0.5rem 0 0 0;
            font-size: 1.1rem;
            opacity: 0.9;
        }
        
        /* Sidebar styling */
        .sidebar .sidebar-content {
            background-color: #f8f9fa;
            border-radius: 10px;
        }
        
        /* Button styling */
        .stButton > button {
            width: 100%;
            background-color: #667eea;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        
        .stButton > button:hover {
            background-color: #5a6fd8;
            border: none;
            transform: translateY(-1px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        
        .stButton > button:active {
            transform: translateY(0);
        }
        
        /* Chat message styling */
        .chat-message {
            padding: 1rem;
            border-radius: 10px;
            margin: 0.5rem 0;
            animation: fadeIn 0.5s ease-in;
        }
        
        .user-message {
            background-color: #e3f2fd;
            border-left: 4px solid #2196f3;
        }
        
        .assistant-message {
            background-color: #f3e5f5;
            border-left: 4px solid #9c27b0;
        }
        
        /* Info box styling */
        .info-box {
            background-color: #e8f5e8;
            padding: 1rem;
            border-radius: 8px;
            border-left: 4px solid #4caf50;
            margin: 1rem 0;
            transition: transform 0.2s ease;
        }
        
        .info-box:hover {
            transform: translateX(5px);
        }
        
        .info-box strong {
            color: #2e7d32;
            display: block;
            margin-bottom: 0.5rem;
        }
        
        /* Custom animations */
        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @keyframes slideIn {
            from {
                transform: translateX(-100%);
            }
            to {
                transform: translateX(0);
            }
        }
        
        /* Sidebar sections styling */
        .sidebar h3 {
            color: #333;
            border-bottom: 2px solid #667eea;
            padding-bottom: 0.5rem;
            margin-bottom: 1rem;
        }
        
        /* Input field styling */
        .stTextInput > div > div > input {
            border-radius: 5px;
            border: 2px solid #e0e0e0;
            transition: border-color 0.3s ease;
        }
        
        .stTextInput > div > div > input:focus {
            border-color: #667eea;
            box-shadow: 0 0 0 0.2rem rgba(102, 126, 234, 0.25);
        }
        
        /* Selectbox styling */
        .stSelectbox > div > div > select {
            border-radius: 5px;
            border: 2px solid #e0e0e0;
        }
        
        /* Checkbox styling */
        .stCheckbox > label {
            font-weight: 500;
            color: #333;
        }
        
        /* Slider styling */
        .stSlider > div > div > div > div {
            background-color: #667eea;
        }
        
        /* Success message styling */
        .stSuccess {
            background-color: #d4edda;
            border: 1px solid #c3e6cb;
            border-radius: 5px;
            color: #155724;
        }
        
        /* Error message styling */
        .stError {
            background-color: #f8d7da;
            border: 1px solid #f5c6cb;
            border-radius: 5px;
            color: #721c24;
        }
        
        /* Warning message styling */
        .stWarning {
            background-color: #fff3cd;
            border: 1px solid #ffeaa7;
            border-radius: 5px;
            color: #856404;
        }
        
        /* Info message styling */
        .stInfo {
            background-color: #d1ecf1;
            border: 1px solid #bee5eb;
            border-radius: 5px;
            color: #0c5460;
        }
        
        /* Spinner styling */
        .stSpinner > div {
            border-top-color: #667eea !important;
        }
        
        /* Chat input styling */
        .stChatInput > div {
            border-radius: 10px;
        }
        
        /* Progress bar styling */
        .stProgress > div > div > div > div {
            background-color: #667eea;
        }
        
        /* Footer styling */
        .footer {
            text-align: center;
            color: #666;
            padding: 1rem;
            border-top: 1px solid #e0e0e0;
            margin-top: 2rem;
        }
        
        .footer a {
            color: #667eea;
            text-decoration: none;
            font-weight: 500;
        }
        
        .footer a:hover {
            color: #5a6fd8;
            text-decoration: underline;
        }
        
        /* Responsive design */
        @media (max-width: 768px) {
            .main-header h1 {
                font-size: 2rem;
            }
            
            .main-header p {
                font-size: 1rem;
            }
            
            .info-box {
                margin: 0.5rem 0;
                padding: 0.8rem;
            }
        }
        
        /* Dark mode support */
        @media (prefers-color-scheme: dark) {
            .info-box {
                background-color: #2d4a2d;
                border-left-color: #4caf50;
            }
            
            .info-box strong {
                color: #81c784;
            }
        }
        
        /* Custom scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
        }
        
        ::-webkit-scrollbar-track {
            background: #f1f1f1;
            border-radius: 4px;
        }
        
        ::-webkit-scrollbar-thumb {
            background: #667eea;
            border-radius: 4px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: #5a6fd8;
        }
        
        /* Loading animation */
        .loading {
            display: inline-block;
            width: 20px;
            height: 20px;
            border: 3px solid #f3f3f3;
            border-top: 3px solid #667eea;
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        /* Tooltip styling */
        .tooltip {
            position: relative;
            display: inline-block;
        }
        
        .tooltip .tooltiptext {
            visibility: hidden;
            width: 120px;
            background-color: #555;
            color: #fff;
            text-align: center;
            border-radius: 6px;
            padding: 5px 0;
            position: absolute;
            z-index: 1;
            bottom: 125%;
            left: 50%;
            margin-left: -60px;
            opacity: 0;
            transition: opacity 0.3s;
        }
        
        .tooltip:hover .tooltiptext {
            visibility: visible;
            opacity: 1;
        }
    </style>
    """, unsafe_allow_html=True)