# Automatizar enviando dados da planilha para preencher os campos mutáveis no certificado padrão


# Pegar os dados da planilha
import openpyxl
from PIL import Image, ImageDraw, ImageFont 
# Abrindo a planilha
workbook_alunos = openpyxl.load_workbook('planilha_alunos.xlsx')
sheet_alunos = workbook_alunos['Sheet1']
# cada célula que contém a informação que preciso
# enumerate retorna um número sequencial para gerar uma imagem com cada nome na sequência
for indice, linha in enumerate(sheet_alunos.iter_rows(min_row=2, max_row=2)):
# Nome do curso, nome participante, tipo de participação, data de início, data do final, carga horária, data de emissão do certificado
  nome_curso = linha[0].value
  nome_participante = linha[1].value
  tipo_participacao = linha[2].value
  data_inicio = linha[3].value
  data_final = linha[4].value
  carga_horaria = linha[5].value
  data_emissao = linha[6].value
  input('')
# Transferir os dados da planilha para a imagem do certificado
  # Importar as fontes
fonte_nome = ImageFont.truetype('./tahoma.ttf',90)
fonte_geral = ImageFont.truetype('./tahomabd.ttf',80)
fonte_data = ImageFont.truetype('./tahoma.ttf',55)
# Abrir a imagem
image = Image.open('./certificado_padrao.jpg')
desenhar = ImageDraw.Draw(image)

desenhar.text((1020, 827),nome_participante, fill='black', font=fonte_nome)
desenhar.text((1060, 950),nome_curso, fill='black', font=fonte_geral)
desenhar.text((1435, 1065),tipo_participacao, fill='black', font=fonte_nome)
desenhar.text((1480, 1182),str(carga_horaria), fill='black', font=fonte_nome)

desenhar.text((750, 1770),data_inicio, fill='black', font=fonte_data)
desenhar.text((750, 1930),data_final, fill='black', font=fonte_data)

desenhar.text((2220, 1930),data_emissao, fill='black', font=fonte_data)

image.save(f'./{indice}{nome_participante}certificado.png')