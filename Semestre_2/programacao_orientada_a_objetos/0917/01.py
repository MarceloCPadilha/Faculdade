
class Aluno:
   def __init__(self, nome, disciplina):
       self.nome = nome
       self.disciplina = disciplina
       # Atributos inicializados como None (Nulos) para validação
       self.nota1 = None
       self.nota2 = None
       self.exame = None

   def lancar_nota1(self, nota1):
       self.nota1 = float(nota1)

   def lancar_nota2(self, nota2):
       self.nota2 = float(nota2)

   def lancar_exame(self, exame):
       self.exame = float(exame)

   def situacao(self):
       # Validação: Verifica se nota1 e nota2 não são nulas
       if self.nota1 is None or self.nota2 is None:
           return 0.0, "Erro: Notas 1 e 2 devem ser lançadas."

       media_inicial = (self.nota1 + self.nota2) / 2
       # Se a média for >= 6  aprovado direto
       if media_inicial >= 6:
           return round(media_inicial, 2), "Aprovado"

       # Se a média < 6, verifica se o exame foi lançado
       if self.exame is None:
           return round(media_inicial, 2), "Em Exame (Aguardando nota)"
       # Cálculo da média final considerando o exame
       media_final = (self.nota1 + self.nota2 + self.exame) / 3
       if media_final >= 6:
           return round(media_final, 2), "Aprovado no Exame"
       else:
           return round(media_final, 2), "Reprovado"

# --- Testando várias situações ---

def exibir_status(aluno):
   media, msg = aluno.situacao()
   print(f"Aluno: {aluno.nome} | Disciplina: {aluno.disciplina}")
   print(f"Notas: [{aluno.nota1}, {aluno.nota2}, {aluno.exame}]")
   print(f"Média: {media} | Situação: {msg}")
   print("-" * 50)


# Caso 1: Notas não lançadas
print("Cenário 1: Notas Faltando")
a1 = Aluno("Ricardo", "Matemática")
exibir_status(a1)

# Caso 2: Aprovado direto
print("Cenário 2: Aprovado Direto")
a2 = Aluno("Ana", "História")
a2.lancar_nota1(8.5)
a2.lancar_nota2(7.5)
exibir_status(a2)

# Caso 3: Em Exame (Aguardando nota)
print("Cenário 3: Notas baixas, sem exame lançado")
a3 = Aluno("Carlos", "Física")
a3.lancar_nota1(4.0)
a3.lancar_nota2(5.0)
exibir_status(a3)

# Caso 4: Aprovado após o exame
print("Cenário 4: Recuperação com sucesso")
a4 = Aluno("Julia", "Química")
a4.lancar_nota1(4.0)
a4.lancar_nota2(5.0)
a4.lancar_exame(9.0) # (4 + 5 + 9) / 3 = 6.0
exibir_status(a4)

# Caso 5: Reprovado mesmo com exame
print("Cenário 5: Reprovado após exame")
a5 = Aluno("Bruno", "Geografia")
a5.lancar_nota1(3.0)
a5.lancar_nota2(2.0)
a5.lancar_exame(5.0) # (3 + 2 + 5) / 3 = 3.33
exibir_status(a5)
