<script setup>
  import TabelaRegistros from '@/components/TabelaRegistros.vue';
  import { ref } from 'vue';

  const gerar_dados_pesquisa = async (palavras_chaves) => {
    try {
      let req = await fetch('http://localhost:8000/pesquisa', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          "palavras_chaves": palavras_chaves
        }),
      });
      let res = await req.json();
      // console.log(res);
      return res;
    } catch (error) {
      console.error('Não foi possivel enviar o formulário:', error);
      throw error;
    }
  };

  const enviarFormulario = async () => {
    try {
      let palavras_chaves = text_input.value.trim().split(' ');
      loading.value = true;
      dados_tabela.value = await gerar_dados_pesquisa(palavras_chaves);
    } catch (error) {
      console.error('Não foi possivel enviar o formulário:', error);
    }
    loading.value = false;
  };

  let text_input = ref('');
  let dados_tabela = ref([]);
  let loading = ref(false);
</script>

<template>
  <main>
    <form class="form-area" @submit.prevent="enviarFormulario">
      <input class="input-form" v-model="text_input" placeholder="pesquisar" />
      <button class="button-form" type="submit">Pesquisar</button>
    </form>
    <TabelaRegistros :dados="dados_tabela" :loading="loading" />
  </main>
</template>

<style scoped>
  main {
    overflow: auto;
    padding-left: 10px;
  }
  .form-area {
    padding: 20px 5px;
  }
  .input-form {
    background-color: transparent;
    color: var(--color-text);
    border: 1px solid var(--color-background-soft);
    padding: 5px 10px;
    border-radius: 5px;
  }
  .input-form:hover {
    background-color: var(--color-background-mute);
  }
  .button-form {
    border: none;
    padding: 5px 10px;
    color: var(--color-text);
    background-color: var(--color-background-soft);
    border-radius: 5px;
    margin-left: 5px;
  }
  .button-form:hover {
    background-color: var(--color-background-mute);
    cursor: pointer;
  }
</style>