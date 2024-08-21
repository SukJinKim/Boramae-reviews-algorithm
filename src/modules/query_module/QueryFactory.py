from .QueryOpenAI import QueryOpenAI
from .QueryAnthropic import QueryAnthropic

class QueryFactory:
    @staticmethod
    def create_query(model_company, api_key):
        if model_company.upper() == "OPENAI":
            return QueryOpenAI(api_key)
        elif model_company.upper() == "ANTHROPIC":
            return QueryAnthropic(api_key)
        else:
            raise ValueError(f"ERR_UNSUPPORTED_MODEL_COMPANY: {model_company}의 모델은 현재 지원하지 않습니다.")
