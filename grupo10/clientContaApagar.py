from SOAPpy import SOAPProxy
# conectando diretamente

servico = SOAPProxy("http://localhost:8010")
print 'Cadastro de Conta a pagar'
codigoApagar = raw_input('codigoApagar: ')
codigoCompra = raw_input('codigoCompra: ')
dataVencimento = raw_input('dataVencimento: ')
dataPagamento = raw_input('dataPagamento: ')
status = raw_input('status: ')
pagar ={'codigoApagar':codigoApagar,'codigoCompra':codigoCompra,'dataVencimento':dataVencimento,'dataPagamento':dataPagamento,'status':status}
if servico.ContasArecebe(pagar):
    print 'Cadastrado com sucesso'
