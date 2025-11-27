function verificarAceiteLGPD() {
    return localStorage.getItem('lgpdAceito') === 'true';
}

function aceitarLGPD() {
    localStorage.setItem('lgpdAceito', 'true');
    document.getElementById('lgpdAlert').style.display = 'none';
    
    mostrarMensagemAceite();
}


function mostrarMensagemAceite() {
    const mensagem = document.createElement('div');
    mensagem.className = 'alert alert-success alert-dismissible fade show fixed-top m-3';
    mensagem.innerHTML = `
        <i class="fas fa-check-circle me-2"></i>
        <strong>Obrigado!</strong> Suas preferências de privacidade foram salvas.
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    document.body.appendChild(mensagem);
    
    setTimeout(() => {
        mensagem.remove();
    }, 3000);
}


function mostrarAvisoLGPD() {
    if (!verificarAceiteLGPD()) {
        document.getElementById('lgpdAlert').style.display = 'block';
    }
}


function revogarConsentimento() {
    localStorage.removeItem('lgpdAceito');
    mostrarAvisoLGPD();
}


document.addEventListener('DOMContentLoaded', function() {
    mostrarAvisoLGPD();
});