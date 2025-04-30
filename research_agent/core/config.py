class Config:
    """配置类,统一管理API密钥和模型参数"""
    # API配置
    ZHIHUIYA_API_KEY = "##"
    API_KEY = "##"
    RERANK_API_KEY = "##"
    WEB_SEARCH_API_KEY = "###"
    # DEFAULT_MODEL = "deepseek-chat"                     # 默认文本生成模型
    WEB_SEARCH_TOP_N = 5
    LANGUAGE='English'
    BATCHSIZE_BIBLIOGRAPHY = 100
    #DEFAULT_MODEL = "deepseek-chat"
    CPM_FOR_SIMPLE_BIBLIOGRAPHY =  20
    CPM_FOR_SEMANTIC_SEARCH = 10
    # DEFAULT_MODEL = "deepseek-chat"
    RERANK_BATCH_SIZE = 10   # 使用llm进行重排时候，设定的batch大小
    SECTION_RAG_TOP_K = 30   #撰写一个section最多用K篇文献
    #DEFAULT_MODEL = "glm-4"
    DEFAULT_MODEL = "volcengine-deepseek-chat"                     # 默认文本生成模型
    EMBEDDING_MODEL = "embedding-3"             # embedding模型
    EMBEDDING_DIMENSIONS = 2048                 # embedding维度
    COS_THRESHOLD = 0.5
    RERANK_THRESHOLD = 19
    MAX_TOKENS = 4095


    #YAML_CONFIG = r"./research_agent/core/llm_config.yaml"            # yaml配置文件路径
    YAML_CONFIG = r"/root/patent_analysis_agent_english_version/research_agent/core/llm_config.yaml"
    # 最大token数
    # 其他配置参数
    TOP_K = 10              # query_by_content返回前多少个相关文档

    THRESHOLD = 0.5        # 重排序相似度阈值,默认0.35
    BATCH_SIZE = 64         # 生成embedding时分批处理数量

    patent_table = "patent_info"

    #language = "English"
    IPC_DICT_PATH = r"###"
    MYSQL_HOST = "##3"
    MYSQL_PORT = 3306
    MYSQL_USERNAME = "###"
    MYSQL_PASSWORD = "####"
    MYSQL_DB = "####"
    MYSQL_CHARSET = "utf8mb4"
    #patent_table = "patent_info"
    language = "English"
    # Word模版文件路径
    #REFERENCE_DOC = r'####'

    # Word模版文件路径
    REFERENCE_DOC = r"####"

