const slides = document.querySelectorAll(".slide");

slides.forEach((slide, indx) => {
    slide.style.transform = `translateX(${indx * 100}%)`;
});

let curSlide = 0;
let maxSlide = slides.length - 1;

// Next slide button functionality
const nextSlide = document.querySelector(".btn-next");

nextSlide.addEventListener("click", function () {
    if (curSlide === maxSlide) {
        curSlide = 0;
    } else {
        curSlide++;
    }

    slides.forEach((slide, indx) => {
        slide.style.transform = `translateX(${100 * (indx - curSlide)}%)`;
    });
});

// previous slide button functionality
const prevSlide = document.querySelector(".btn-prev");

// add event listener and navigation functionality
/* prevSlide.addEventListener("click", function () {
    // check if current slide is the first and reset current slide to last
    if (curSlide === 0) {
        curSlide = maxSlide;
    } else {
        curSlide -;
    }

    //   move slide by 100%
    slides.forEach((slide, indx) => {
        slide.style.transform = `translateX(${100 * (indx - curSlide)}%)`;
    });
}); */