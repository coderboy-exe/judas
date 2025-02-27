import os
import sys
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
print(OPENAI_API_KEY)

from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index.llms import OpenAI


documents = SimpleDirectoryReader('data').load_data()
llm = OpenAI(temperature=0, model="text-davinci-003")
service_context = ServiceContext.from_defaults(llm=llm)
index = VectorStoreIndex.from_documents(documents)
# print(index)

def run_index(content):
    query_engine = index.as_query_engine(service_context=service_context)
    print(query_engine)
    response = query_engine.query("What are the most relevant keywords and their corresponding categories in the format [category: keyword(s); category: keyword(s), ...]. If a category is not included in the provided article, write [category: None]. DO NOT INCLUDE the template context in your responses(e.g People: Joe Biden, Elon Musk, Angela Merkel; Organizations: United Nations, Google, World Health Organization; Events: Olympics, Presidential Election, Hurricane Ida; Issues: Climate Change, Immigration, Income Inequality, Cybersecurity; Policies and Laws: Affordable Care Act, GDPR, Net Neutrality; Industries and Sectors: Automotive, Energy, Financial Services, Agriculture; Products and Services: iPhone, Tesla Model S, 5G; Emotions and Sentiment: Positive, Negative, Neutral; Timeframe: 2020, Q1, Monthly, Annual). The content to analyze is the one in the brackets '()' after the colon: " + f"({content})")

    stripped = str(response).strip().replace('\n', '')
    # print(stripped)
    return stripped

# run_index("tWorld Youth Skills Day: Stakeholders Harp On Youth Employment Through Vocational Digital Education by Abdullahi Olesin 2 hours ago in News  Photo by Javon Swaby from Pexels Share on WhatsAppShare on FacebookShare on TwitterTelegram  Stakeholders have stressed the need for the government at all levels to make concerted efforts at bridging the skills gap among Nigerian youths through mass vocational digital education.Stakeholders which included the representatives of the Small and Medium Enterprises Development Agency of Nigeria (SMEDAN), National Directorate for Employment (NDE) the National Youth Service Corps (NYSC), Kwara State Chambers for Commerce and Industry (KWACCIMA) and the Nigeria Labour Congress (NLC), bared their minds at an event organised by the Michael Imoudu National Institute For Labour Studies (MINILS), Ilorin to mark the 2023 World Youth Skills Day (WYSD).The United Nations General Assembly in 2014 declared 15th July as the World Youth Skills Day, with the objective of bringing to the fore the strategic importance of equipping young people with required skills for employment and entrepreneurship.The theme for 2023 World Youth Skills Day is ‘Skilling Teachers, Trainers and Youth for Transformative Future’.The theme essentially highlights the roles of teachers and trainers in technical and vocational education and training (TVET), in institutions responsible for transferring relevant skills to the youth.At the event, the director general of MINILS, Ilorin Kwara State, Comrade Issa Aremu, hailed the renewed commitment of President Bola Tinubu’s administration to bridge the skills gap among youths through mass youth vocational digital education.RELATED   JNI To Federal Govt: Secure Nigeria, Crush Terrorists, Bandits, Kidnappers 5 mins ago  JUST-IN: NAF Airstrikes Kill 22 Terrorists Loyal To Slain Katsina Bandit Kingpin 8 mins ago     He observed that the critical component of the renewed hope agenda of Tinubu is youth employability through skills acquisition.The director general called on all stakeholders in the labour market to collaborate with the federal government to train and retrain youths for sustainable jobs and poverty eradication.“As the world undergoes rapid technology, economic and social transformations, young people need the right skills while the teachers and trainers stand at the forefront of these great global efforts, and need to be well equipped to deliver” Aremu said.For his part, the chairman of NLC in Kwara State, Comrade Murtala Okayinka, emphasised need for government to roll out measures that will propel youths to embrace skills acquisition.He says that white collar jobs were no longer available, adding that the only way youths can become self-employed and even employers of labour, is vocational study and skills acquisition.The NLC chairman praised the management of MINILS for drawing the attention of government to the need for a re-orientation of Nigerian youths through the programme.Also speaking, the president of KWACCIMA, Mr Fatai Ayodimeji, aligned himself with submission of the MINILS’s director general and state NLC chairman.He reasoned that since white collar jobs were no longer in existence, government should encourage youths to take interest in skill acquisition.He tasked MINILS to go beyond talkshow by encouraging youths who were into businesses, to exhibit their products in subsequent editions of the programe.Ayodimeji later announced that KWACCIMA would sponsor the trade exhibition aspect of activities marking World Youth Skills Day next year.")

def summarize(content):
    """ Make the summary request """
    template = (f"Please summarize the article enclosed in brackets after the colon accurately and intelligently in exactly sixty(60) words: \n ({content})")
    response = OpenAI(temperature=0, model="text-davinci-003").complete(template)

    # print(response)
    return response


def rewrite_tv(content):
    """ Rewrite content for TV presentation """
    template = (f"Please rewrite the main content of this article enclosed in brackets after the colon intelligently (in English) for TV presentation: \n ({content})")
    response = OpenAI(temperature=0, model="text-davinci-003").complete(template)

    # print(response)
    return response


def rewrite_radio(content):
    """ Rewrite content for TV presentation """
    template = (f"Please rewrite the main content of this article enclosed in brackets after the colon intelligently (in English) for a Radio presentation: \n ({content})")
    response = OpenAI(temperature=0, model="text-davinci-003").complete(template)

    # print(response)
    return response


def rewrite_online(content):
    """ Rewrite content for TV presentation """
    template = (f"Please rewrite the main content of this article intelligently (in English) for an online presentation. DO NOT talk about 'Sign Up' or 'Register': \n {content}")
    response = OpenAI(temperature=0, model="text-davinci-003").complete(template)

    # print(response)
    return response

