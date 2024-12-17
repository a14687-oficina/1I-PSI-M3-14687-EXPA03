# 1I-PSI-M3-14687-EXPA03
 <h1>Descrição do Código - Programa de Gestão de Stock</h1>
    <p>Este código implementa um programa de gestão de stock em Python, permitindo ao usuário registrar materiais, verificar a quantidade disponível, atualizar o stock e exportar o estado geral do stock para um arquivo de texto.</p>
    <h2>Como Funciona</h2>
    <ol>
        <li>O programa define várias funções para gerenciar o stock:</li>
        <ul>
            <li><code>registrar_material(stock)</code>: Permite ao utilizador registrar um novo material e sua quantidade. Se o material já estiver registrado, uma mensagem é mostrada dizendo que o material já está registrado.</li>
            <li><code>verificar_stock(stock)</code>: Permite ao utilizador consultar a quantidade de um material específico no stock.</li>
            <li><code>atualizar_stock(stock)</code>: Permite ao utilizador adicionar ou remover quantidades de um material já registrado. O utilizador deve dizer o que quer fazer (adicionar ou remover) e a quantidade.</li>
            <li><code>mostrar_stock(stock, filename='Stock.txt')</code>: Exporta o estado atual do stock para um arquivo de texto, listando todos os materiais e suas quantidades.</li>
        </ul>
        <li>A função <code>main()</code> controla o programa, mostrando um menu com opções para o usuário:</li>
        <ul>
            <li>Registrar Material</li>
            <li>Verificar Stock de um material</li>
            <li>Atualizar o Stock</li>
            <li>Verificar Stock Geral</li>
            <li>Sair</li>
        </ul>
        <li>O programa continua a funcionar até que o usuário escolha a opção de sair.</li>
    </ol>
