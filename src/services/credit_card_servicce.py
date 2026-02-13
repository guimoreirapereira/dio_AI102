from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyseDocumentRequest
from utils.Config import Config

def analyse_credit_card(card_url):

    try:
        credential = AzureKeyCredential(Config.KEY)
        document_client = DocumentIntelligenceClient(Config.ENDPOINT, credential)

        card_info = document_client.begin_analyze_document(
            "prebuilt_creditcard", AnalyseDocumentRequest(url_source = card_url)
        )
        result = card_info.result()

        return result
    except Exception as ex:
        return None

                                                           






