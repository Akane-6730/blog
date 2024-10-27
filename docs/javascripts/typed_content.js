var sentences = [
  '人間は思い出がないと生きていけないんだよ。',
  'でもね、それなのに思い出だけでも生きていけない。',
  '夢はいつか覚めないといけない。',
  '覚めない夢はいつか悲しみに変わっちゃうから…'
];

var index = 0;

function typeNextSentence() {
  if (index < sentences.length) {
    var typed = new Typed('#typed-des', {
      strings: [sentences[index]],
      typeSpeed: 70,
      backSpeed: 0,
      cursorChar: '_',
      smartBackspace: true,
      loop: false,
      onComplete: function() {
        index++;
        setTimeout(typeNextSentence, 3000); // 每句后停顿3秒
      }
    });
  }
}

typeNextSentence();