Reveal.initialize({
  hash: true,
  controls: true,
  progress: true,
  slideNumber: 'c/t',
  center: true,
  width: 1280,
  height: 720,
  margin: 0.055,
  transition: 'slide',
  backgroundTransition: 'fade',
  autoAnimate: true,
  autoAnimateDuration: 0.8,
  autoAnimateEasing: 'ease-out',
  pdfSeparateFragments: false,
  plugins: [ RevealNotes, RevealHighlight, RevealMath.KaTeX, RevealSearch, RevealZoom ]
});
