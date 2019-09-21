from flask import Flask, jsonify, request
from flask_cors import CORS
import nltk
import os

app = Flask(__name__)
CORS(app)
base = [
        #Felicidade
        ('Hoje o dia está incrível', 'Felicidade'),
        ('Como a minha vida é bela', 'Felicidade'),
        ('Eu sou muito feliz', 'Felicidade'),
        ('Hoje o dia está incrível', 'Felicidade'),
        ('Eu quero estar sempre com você', 'Felicidade'),
        ('Você é a razão da minha felicidade', 'Felicidade'),
        ('Estou muito feliz por estar com você', 'Felicidade'),
        ('Tudo é incrível', 'Felicidade'),
        ('É tudo tão belo', 'Felicidade'),
        ('eu sou admirada por muitos','Felicidade'),
        ('me sinto completamente amado','Felicidade'),
        ('amar é maravilhoso','Felicidade'),
        ('estou me sentindo muito animado novamente','Felicidade'),
        ('eu estou muito bem hoje','Felicidade'),
        ('que belo dia para dirigir um carro novo','Felicidade'),
        ('o dia está muito bonito','Felicidade'),
        ('estou contente com o resultado do teste que fiz no dia de ontem','Felicidade'),
        ('o amor é lindo','Felicidade'),
        ('nossa amizade e amor vai durar para sempre', 'Felicidade'),
        ('eu gosto de mc donalds','Felicidade'),
        ('eu gosto muito de hambúrguer','Felicidade'),
        ('eu amo mcdonalds','Felicidade'),
        ('hoje estou me sentindo amável','Felicidade'),
        ('não consigo parar de pensar em você','Felicidade'),
        ('sinto sua falta','Felicidade'),
        ('eu te amo','Felicidade'),
        ('feliz','Felicidade'),
        ('felicidade','Felicidade'),
        ('você faz meu dia melhor','Felicidade'),
        ('você é o que me falta','Felicidade'),
        ('amor é fogo que arde sem se ver','Felicidade'),
        ('eu te amo','Felicidade'),
        ('não consigo passar um dia sem lhe ver','Felicidade'),
        ('eu te amo tanto','Felicidade'),
        ('Tenho em mim todos os sonhos do mundo','Felicidade'),
        ('estou alegre','Felicidade'),
        ('fico feliz de reencontrar você','Felicidade'),
        ('que alegria','Felicidade'),
        ('Que alegria rever você','Felicidade'),
        ('que ótimo final de semana','Felicidade'),
        ('como é bom revelo','Felicidade'),
        ('feliz aniversário','Felicidade'),
        ('Tenho em mim todos os sonhos do mundo','Felicidade'),
        ('somos campeões','Felicidade'),
        ('alegremente','Felicidade'),
        ('que bom estar aki','Felicidade'),
       ('vamos festejar','Felicidade'),
       ('vamos pular','Felicidade'),
       ('sorridente','Felicidade'),
       ('sorrir','Felicidade'),
       ('que divertido','Felicidade'),
       ('Vamos nos divertir','Felicidade'),
       ('Alegre-se','Felicidade'),
       ('Como é bom estar com você','Felicidade'),
       ('Como foi divertido ir no parque','Felicidade'),
       ('Tenho em mim todos os sonhos do mundo','Felicidade'),
       ('O céu está tão estrelado','Felicidade'),
        ('Tenho em mim todos os sonhos do mundo','Felicidade'),
        ('O céu está tão estrelado','Felicidade'),
       ('Tenho em mim todos os sonhos do mundo','Felicidade'),
       ('Não há nada em que me deixe mais alegre','Felicidade'),
       ('Viver a vida dessa forma me deixa muito alegre','Felicidade'),
       ('Alegria de viver está em sentir gratidão por todos os momentos da vida, mesmo os ruins','Felicidade'),
       ('Eu quero ser alegre a vida inteira','Felicidade'),
       ('Sorrir torna tudo mais alegre','Felicidade'),
       ('Alegre','Felicidade'),




        #Medo
        ('Se ela descobrir que fui eu, eu estou ferrado', 'Medo'),
        ('Tomara que ela não descubra', 'Medo'),
        ('Eu estou arrepiado', 'Medo'),
        ('Tomara que não me veja', 'Medo'),
        ('Por favor fica longe de mim', 'Medo'),
        ('Sai, sai, fica longe de mim', 'Medo'),
        ('Por favor, o que eu fiz pra você, me deixa em paz', 'Medo'),
        ('Por favor para, me deixa em paz', 'Medo'),
        ('Eu não fiz nada pra você, me deixar ir, plese.', 'Medo'),
        ('medo', 'Medo'),
        ('assustado', 'Medo'),
        ('estou amedrontado', 'Medo'),
        ('fiquei com medo', 'Medo'),
        ('me deu muito medo', 'Medo'),
        ('ele está me ameaçando a dias', 'Medo'),
        ('isso me deixa apavorada', 'Medo'),
        ('este lugar e apavorante', 'Medo'),
        ('se perdermos outro jogo seremos eliminados e isso me deixa com pavor', 'Medo'),
        ('tome cuidado com o lobisomem', 'Medo'),
        ('se eles descobrirem estamos encrencados', 'Medo'),
        ('estou tremendo de medo', 'Medo'),
        ('eu tenho muito medo dele', 'Medo'),
        ('estou com medo do resultado dos meus testes', 'Medo'),


        #Tristeza
        ('Porque minha vida é tão sem graça', 'Tristeza'),
        ('Eu estou triste', 'Tristeza'),
        ('Eu sou merda meu irmão', 'Tristeza'),
        ('Minha vida é uma merda', 'Tristeza'),
        ('Nada de bom acontece comigo', 'Tristeza'),
        ('Sempre me dou mal em tudo', 'Tristeza'),
        ('Como eu sou um lixo', 'Tristeza'),
        ('Eu queria ver você', 'Tristeza'),
        ('Eu não consigo viver sem você', 'Tristeza'),
        ('Nunca faço nada direito', 'Tristeza'),
        ('Sempre me dou mal em tudo, porque?', 'Tristeza'),
        ('estou me sentindo triste','Tristeza'),
        ('eu sou muito infeliz', 'Tristeza'),
        ('perdemos um jogo ontem a noite','Tristeza'),
        ('ele me deixou sozinha','Tristeza'),
        ('hoje acordei triste','Tristeza'),
        ('triste','Tristeza'),
        ('tristeza','Tristeza'),
        ('hoje estou me sentindo meio para baixo','Tristeza'),
        ('me sinto só','Tristeza'),
        ('por que ninguém me ama','Tristeza'),
        ('queria ser amada','Tristeza'),
        ('me sinto sozinho','Tristeza'),
        ('hoje acordei com vontade de ficar na cama','Tristeza'),
        ('sinto sua falta','Tristeza'),
        ('meu amor não é compreensível','Tristeza'),
        ('eu não consegui','Tristeza'),
        ('desisto','Tristeza'),
        ('que se foda, desisto','Tristeza'),
        ('eu não consigo','Tristeza'),
        ('eu não vou conseguir mesmo','Tristeza'),
        ('ele não conseguiu fazer isso','Tristeza'),
        ('Minha vida é injusta','Tristeza'),
	  ('porque sempre acontece esse tipo de coisa comigo','Tristeza'),
	  ('ele não consigo responder essa questão','Tristeza'),
        ('Eu sou um merda meu irmão','Tristeza'),
        ('ele foi tão grosso comigo','Tristeza'),
	  ('eu achei que ele me amava','Tristeza'),
        ('ele me iludiu','Tristeza'),
	  ('fui enganada de novo','Tristeza'),
	  ('nunca me senti tão sozinha','Tristeza'),
	  ('estou triste por não ter ninguém ao meu lado','Tristeza'),
	  ('estou sempre sozinha','Tristeza'),


        #Nojo
        ('Eca, que nojo', 'Nojo'),
	   ('credo que nojo', 'Nojo'),
        ('Para com essa nojeira', 'Nojo'),
        ('como você é nojenta', 'Nojo'),
        ('Isso é nojento', 'Nojo'),
        ('Que desagradável ver você comer', 'Nojo'),
        ('nojento', 'Nojo'),
        ('Que nojeira', 'Nojo'),
        ('nojo', 'Nojo'),
        ('Aaahhh, que nojenta, para', 'Nojo'),
        ('Ugh, não aguento nem olhar', 'Nojo'),
        ('Que coisa desagradável de se olhar', 'Nojo'),
        ('Que nojento', 'Nojo'),
        ('Não aguento nem olhar essa nojeira', 'Nojo'),
        ('Para de fazer isso, é nojento', 'Nojo'),
        ('Para de nojeira', 'Nojo'),
        ('Que merda é essa, coisa nojenta', 'Nojo'),
	  ('Haaa, tira isso da minha frente', 'Nojo'),
        ('Que nojo', 'Nojo'),
        ('Credo', 'Nojo'),
        ('Aff, que nojo', 'Nojo'),
        ('Que coisa nojenta, para com isso', 'Nojo'),
	   ('para com isso nojento', 'Nojo'),



        #Raiva
        ('Eu vou acabar com você', 'raiva'),
        ('Como eu estou irritado', 'raiva'),
        ('Eu odeio você', 'raiva'),
        ('Eu odeio tudo', 'raiva'),
        ('Tomara que você se ferre', 'raiva'),
        ('Eu não gosto de você', 'raiva'),
        ('Tomara que você morra', 'raiva'),
        ('Sai de perto de mim', 'raiva'),
        ('Vai se fuder', 'raiva'),
        ('Eu quero você longe de mim', 'raiva'),
        ('Eu te odeio', 'raiva'),
        ('Min odiar você', 'raiva'),
        ('Nunca mais apareça na minha frente', 'raiva'),
        ('Não quero mais ver você perto de mim', 'raiva'),
        ('Anão, tu de novo, me esqueça', 'raiva'),
        ('Desapareça da minha vida', 'raiva'),
        ('Suma daqui antes que eu acabe com você', 'raiva'),
        ('Filho da p%ta', 'raiva'),
        ('Te odeio', 'raiva'),
        ('Eu te odeio do fundo do meu coração', 'raiva'),
        ('morra', 'raiva'),
        ('desejo que você morra, e vá para o quinto dos infernos', 'raiva'),
        ('ódio', 'raiva'),
        ('odiar', 'raiva'),
        ('vai se fude', 'raiva'),
        ('Sai de perto de mim', 'raiva'),
	  ('Hoje estou puto', 'raiva'),
        ('eu odeio prova', 'raiva'),
        ('Você s me faz passar raiva', 'raiva'),
	 ('Bicho, como você é irritante', 'raiva'),
       ('Nunca mais apareça na minha frente', 'raiva'),
       ('Se eu tive de novo, te dou um murro', 'raiva'),
       ('Sai da minha frente ou te dou um soco', 'raiva'),
	 ('Desapareça da minha frente', 'raiva'),
       ('Da próxima vez que eu lhe ver, vou acabar com você', 'raiva'),
	 ('Mano, vai tomar no cu', 'raiva'),
       ('Arrombado', 'raiva'),
       ('Filho da puta', 'raiva'),
       ('Desgraçado', 'raiva'),
	 ('Moleque', 'raiva'),
       ('Sai disgraça', 'raiva'),
       ('Como eu odeio você', 'raiva'),
       ('irritado', 'raiva'),
        
        #Surpresa
        ('Por essa eu não esperava', 'Surpresa'),
        ('Caraca', 'Surpresa'),
        ('Que massa', 'Surpresa'),
        ('Que susto,fiquei arrepiado' , 'Surpresa'),
        ('Incrível', 'Surpresa'),
        ('Aff, que susto', 'Surpresa'),
        ('Você me surpreendeu com isso', 'Surpresa'),
        ('Que surpresa, nunca ia adivinhar', 'Surpresa'),
        ('Surpreendente', 'Surpresa'),
        ('Surpresa', 'Surpresa'),
        ('Bolo!!', 'Surpresa'),
        ('aaaaaaaaaaaa', 'Surpresa'),
        ('Me surpreendeu isso', 'Surpresa'),
        ('Que susto', 'Surpresa'),
        ('Me assustei', 'Surpresa'),
        ('Taram', 'Surpresa'),
        ('Me assustou, quase que tive um ataque no coração', 'Surpresa'),
        ('Surpresa, feliz aniversário', 'Surpresa'),
        ('Assim voçe me mata do coração', 'Surpresa'),
        ('Estou surpreso', 'Surpresa')]

stopwordsnltk=nltk.corpus.stopwords.words('portuguese')

def stem(texto):
    stemm = nltk.stem.RSLPStemmer()
    frasesstemming=[]
    for(palavras, emocao) in texto:
        comstem=[str(stemm.stem(p)) for p in palavras.split() if p not in stopwordsnltk]
        frasesstemming.append((comstem, emocao))
    return frasesstemming
frasescomstemin = stem(base)
#print(frasescomstemin)

def busca_palavra(frases):
    todaspalavras=[]
    for (palavras,emocao) in frases:
        todaspalavras.extend(palavras)
    return todaspalavras
palavras=busca_palavra(frasescomstemin)

#print(palavras)

def busca_freq(palavras):
    palavras = nltk.FreqDist(palavras)
    return palavras
frequencia = busca_freq(palavras)
#print(frequencia.most_common(50))

def busca_unicas(frequencia):
    freq=frequencia.keys()
    return freq
unicas = busca_unicas(frequencia)
#print(unicas)

def extrair(documento):
    doc = set(documento)
    caract = {}
    for palavras in unicas:
        caract['%s'%palavras]= (palavras in doc)
    return caract
caracteres=extrair(['am','nov','dia'])


@app.route("/")
def hello_world():
    return "Hello World! <strong>I am learning Flask</strong>", 200

@app.route("/texto/<string:teste>", methods=['GET'])
#def hello_world2(num):
#   return jsonify({'Resultado':num+10}), 200



def testeabc(teste):

    basecompleta = nltk.classify.apply_features(extrair, frasescomstemin)
    classificador = nltk.NaiveBayesClassifier.train(basecompleta)
    testem = []
    stemm = nltk.stem.RSLPStemmer()
    for (palavras) in teste.split():
        comstem=[p for p in palavras.split()]
        testem.append(str(stemm.stem(comstem[0])))
   
        novo = extrair(testem)
    
    
    return jsonify({'Resultado':classificador.classify(novo)}), 200


if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0',port=port)
