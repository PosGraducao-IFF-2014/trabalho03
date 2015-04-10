#-*- encoding: iso-8859-1 -*-
from SOAPpy import SOAPServer
from SOAPpy import SOAPProxy
db = 'pagar.txt'
def ContasArecebe(pagar):
    if consultarApagar(pagar['codigoApagar']):
        return False
    conexao = open(db,'a')
    conexao.write('%s|%s|%s|%s|%s\n' % (pagar['codigoApagar'],pagar['codigoCompra'], pagar['dataVencimento'], pagar['dataPagamento'], pagar['status']))
    conexao.close()
    return True

def consultarApagar(pconsulta):
    try:
        linhas = open(db,'r').read()
        f = open(db,"r")
        linhas = f.readlines()
        for linha in linhas:
            codigoApagar,codigoCompra,dataVencimento,dataPagamento, status = linha.split('|')

        if ( pconsulta == codigoApagar ):
            return True
        f.close()
        return False
    except:
        return False

def deletarApagar(codigoR):
    try:
        servico = SOAPProxy("http://localhost:8010")
        f = open(db,"r")
        lines = f.readlines()
        f.close()
        f = open(db,"w")

        for linha in linhas:
            codigoApagar,codigoCompra,dataVencimento,dataPagamento, status = linha.split('|')

        if codigoApagar != codigoR:
            f.write(linha)
            f.close()
        return True
    except:
        return False

serv = SOAPServer(("localhost", 8010))
serv.registerFunction(ContasArecebe)
serv.registerFunction(consultarApagar)
serv.registerFunction(deletarApagar)
serv.serve_forever()
