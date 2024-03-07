import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { ScrollToPlugin } from "gsap/ScrollToPlugin";
import { SplitText } from "gsap/SplitText";

gsap.registerPlugin(ScrollTrigger, ScrollToPlugin);

const split = new SplitText("#title", {type:"chars"});

gsap.from("#woman", {
  scrollTrigger: {
    trigger: "#woman",
    scrub: true,
  },
  y: 50,
});

gsap.from("#leftplant", {
  scrollTrigger: {
    trigger: "#leftplant",
    scrub: true,
  },
  x: -150,
});

gsap.from("#rightplant", {
  scrollTrigger: {
    trigger: "#rightplant",
    scrub: true,
  },
  x: 150,
});

gsap.from("#ball", {
  scrollTrigger: {
    trigger: "#ball",
    scrub: true,
  },
  x: -200,
});

gsap.from("#lifebuoy", {
  scrollTrigger: {
    trigger: "#lifebuoy",
    scrub: true,
  },
  x: 200,
});

gsap.timeline({
  scrollTrigger: {
    trigger: ".parallax",
    start: "top 50%",
    end: "bottom top",
    toggleActions: "restart none none reset",
  },
})
.from(split.chars, {
  yPercent: -150,
  stagger: 0.05,
  duration: 0.7,
  ease: "back",
})
.from(split.chars, { opacity: 0, delay: 0.05, stagger: 0.05, duration: 0.2 }, 0);


// js for loading
// function startBuffering() {
//   console.log("ok")
//   document.getElementById("bufferingRing").style.display = "block";
// }
// js for loading end here 
