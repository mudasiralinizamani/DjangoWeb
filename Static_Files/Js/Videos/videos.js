// This Javascript is for manupulating tabs on Video Page

const tabs = document.querySelectorAll(".tabs li");
const tabscontentboxes = document.querySelectorAll("#tab-content > div");

tabs.forEach((tab) => {
  tab.addEventListener("click", () => {
    tabs.forEach((item) => item.classList.remove("is-active"));
    tab.classList.add("is-active");

    const target = tab.dataset.target;

    tabscontentboxes.forEach((box) => {
      if (box.getAttribute("id") === target) {
        box.classList.remove("is-hidden");
      } else {
        box.classList.add("is-hidden");
      }
    });
  });
});