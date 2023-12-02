let windowHeight = window.innerHeight;
let windowHeightExtra = 0;
const safari = /^((?!chrome|android).)*safari/i.test(navigator.userAgent);
const mobile = /Mobi/.test(navigator.userAgent);
safari &&
  !mobile &&
  (windowHeightExtra = window.outerHeight - window.innerHeight),
  mobile &&
    ((windowHeight = window.screen.availHeight),
    (windowHeightExtra = (window.screen.availHeight - window.innerHeight) / 2));
const positionParallax = function (e, t, a, i) {
  const n = e.top / t - windowHeightExtra;
  a[i].style.top = `${n}px`;
};
const animateParallax = function (e, t) {
  for (let a = 0; e.length > a; a++) {
    const i = e[a].parentElement.parentElement.getBoundingClientRect();
    i.top + i.height >= 0 &&
      i.top <= windowHeight &&
      positionParallax(i, t, e, a);
  }
};
const calculateHeight = function (e, t) {
  for (let a = 0; e.length > a; a++) {
    const i = e[a].parentElement.parentElement.getBoundingClientRect();
    const n = e[a].parentElement.parentElement.offsetTop;
    const o = (windowHeight - i.height) / 2;
    const r =
      windowHeight > i.height + n
        ? i.height + n - n / t
        : i.height + 2 * (o - o / t);
    (e[a].style.height = `${r + 2 * windowHeightExtra}px`),
      positionParallax(i, t, e, a);
  }
};
const universalParallax = function () {
  this.init = function (i) {
    void 0 === i && (i = {}),
      (i = {
        speed: void 0 !== i.speed ? i.speed : 1.5,
        className: void 0 !== i.className ? i.className : "parallax",
      });
    for (
      var n = document.getElementsByClassName(i.className), e = 0;
      n.length > e;
      e++
    ) {
      const t = document.createElement("div");
      n[e].parentNode.insertBefore(t, n[e]), t.appendChild(n[e]);
      const a = n[e].parentElement;
      (a.className += "parallax__container"),
        window
          .getComputedStyle(a.parentElement, null)
          .getPropertyValue("position") !== "relative" &&
          (a.parentElement.style.position = "relative");
      const o = n[e].dataset.parallaxImage;
      void 0 !== o &&
        ((n[e].style.backgroundImage = `url(${o})`),
        n[e].classList.length === 1 &&
          n[e].classList[0] === "parallax" &&
          ((n[e].style.backgroundRepeat = "no-repeat"),
          (n[e].style.backgroundPosition = "center"),
          (n[e].style.backgroundSize = "cover")));
    }
    document.addEventListener("readystatechange", (e) => {
      let t;
      let a;
      e.target.readyState === "complete" &&
        ((t = n),
        (a = i.speed) < 1 && (a = 1),
        calculateHeight(t, a),
        mobile ||
          window.addEventListener("resize", () => {
            (windowHeight = window.innerHeight), calculateHeight(t, a);
          }),
        window.addEventListener("scroll", () => {
          animateParallax(t, a);
        }));
    });
  };
};
new universalParallax().init({
  speed: 3,
});
