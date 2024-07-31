class SistemaEscolar {
    mostrarMenu() {
        const menu = `
        ====================
           SISTEMA ESCOLAR
        ====================
        1. Cadastrar novo estudante
        2. Listar todos os estudantes
        3. Atualizar dados de um estudante
        4. Excluir um estudante
        5. Sair
        ====================
        `;
        console.log(menu);
    }

    opcaoInvalida() {
        console.log("Opção inválida, por favor selecione uma opção válida.");
    }

    main() {
        // Aqui você pode adicionar lógica para controlar as opções do menu.
        // Por exemplo, capturar a entrada do usuário e chamar o método correspondente.
    }
}

// Instanciando a classe e chamando o método main.
const sistema = new SistemaEscolar();
sistema.main();
