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
    <form @submit.prevent="enviarFormulario">
      <input v-model="text_input" />
      <button type="submit">Pesquisar</button>
    </form>
    <TabelaRegistros :dados="dados_tabela" :loading="loading" />
  </main>
</template>
