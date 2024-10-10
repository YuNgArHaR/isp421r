var e = document.querySelectorAll(".slider__img");
let i = 0;

if (e) {
  void setInterval(() => {
    e[i].style.zIndex = 0;

    i++;

    i = i === e.length ? 0 : i;

    e[i].style.zIndex = 1;
  }, 2000);
}
