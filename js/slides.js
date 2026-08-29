Reveal.initialize({
  hash: true,
  controls: true,
  progress: true,
  center: false,
  slideNumber: 'c/t',
  transition: 'slide',
  backgroundTransition: 'fade',
  width: 1280,
  height: 720,
  margin: 0.055,
  minScale: 0.2,
  maxScale: 2,
  autoAnimate: true,
  autoAnimateDuration: 0.8,
  plugins: [ RevealNotes, RevealHighlight, RevealMath.KaTeX, RevealSearch, RevealZoom ]
});

document.querySelectorAll('.quiz').forEach((quiz) => {
  const feedback = quiz.querySelector('.feedback');
  quiz.querySelectorAll('button').forEach((button) => {
    button.addEventListener('click', () => {
      const isRight = button.dataset.answer === 'right';
      feedback.textContent = isRight
        ? 'Correto: esse padrão indica gap entre memorização e generalização.'
        : 'Ainda não: observe a diferença entre erro de treino e validação.';
      feedback.className = `feedback ${isRight ? 'good' : 'bad'}`;
    });
  });
});

Reveal.on('slidechanged', (event) => {
  const title = event.currentSlide.querySelector('h1,h2')?.textContent?.trim() || 'slide';
  document.title = `${title} · Unidade 1`;
});
