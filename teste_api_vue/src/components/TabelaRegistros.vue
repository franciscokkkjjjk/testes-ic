<script setup>
defineProps({
  dados: {
    type: Array[Object],
    required: true
  },
  loading: {
    type: Boolean,
    required: true
  }
})
</script>

<template>
  <div class="table-area">
    <table class="tabela" border="1">
      <thead>
        <tr>
          <th scope="col">Registro ANS</th>
          <th scope="col">CNPJ</th>
          <th scope="col">Razao Social</th>
          <th scope="col">Modalidade</th>
          <th scope="col">Logradouro</th>
          <th scope="col">Numero</th>
          <th scope="col">Complemento</th>
          <th scope="col">Bairro</th>
          <th scope="col">Cidade</th>
          <th scope="col">UF</th>
          <th scope="col">CEP</th>
          <th scope="col">DDD</th>
          <th scope="col">Telefone</th>
          <th scope="col">Fax</th>
          <th scope="col">Endereco Eletronico</th>
          <th scope="col">Representante</th>
          <th scope="col">Cargo Representante</th>
          <th scope="col">Regiao de Comercializacao</th>
          <th scope="col">Data de registro na ANS</th>
        </tr>
      </thead>
      <tbody v-if="!loading">
        <tr v-for="linha in dados" :key="linha.Registro_ANS">
          <th scope="row">{{ linha.Registro_ANS }}</th>
          <td scope="row">{{ linha.cnpj }}</td>
          <td scope="row">{{ linha.razao_social }}</td>
          <td scope="row">{{ linha.modalidade }}</td>
          <td scope="row">{{ linha.logradouro }}</td>
          <td scope="row">{{ linha.numero }}</td>
          <td scope="row">{{ linha.complemento }}</td>
          <td scope="row">{{ linha.bairro }}</td>
          <td scope="row">{{ linha.cidade }}</td>
          <td scope="row">{{ linha.uf }}</td>
          <td scope="row">{{ linha.cep }}</td>
          <td scope="row">{{ linha.ddd }}</td>
          <td scope="row">{{ linha.telefone }}</td>
          <td scope="row">{{ linha.fax }}</td>
          <td scope="row">{{ linha.endereco_eletronico }}</td>
          <td scope="row">{{ linha.representante }}</td>
          <td scope="row">{{ linha.cargo_representante }}</td>
          <td scope="row">{{ linha.regiao_de_comercializacao }}</td>
          <td scope="row">{{ linha.data_registro_ans }}</td>
        </tr>
      </tbody>
      <tr v-if="loading">
        <td class="area-load" colspan="19">
          <div class="carregando"></div>
        </td>
      </tr>
    </table>
  </div>
</template>

<style scoped>
.table-area {
  max-width: 99%;
  max-height: 89%;
  overflow: auto;
}
.area-load {
  text-align: center;
}
.area-load > .carregando {
  display: inline-block;
  width: 30px;
  height: 30px;
  margin: 5px;
}
.tabela {
  background-color: var(--color-background-mute);
}
.tabela,
th,
td {
  border-collapse: collapse;
  text-align: left;
  font-size: 13px;
  border: none;
}
thead {
  background-color: var(--color-background-soft);
}
tbody > tr:hover {
  background-color: var(--color-background-soft);
}
th,
td {
  padding: 5px;
}
</style>
