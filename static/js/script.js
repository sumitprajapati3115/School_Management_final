const toggle = document.querySelector(".menu-toggle");
const nav = document.querySelector("nav");
const links = document.querySelectorAll("nav ul li a");
toggle.onclick = () => {
  nav.classList.toggle("active");
};
links.forEach(link => {
  link.onclick = () => {
    nav.classList.remove("active");
  };
});

// GALLERY LIGHTBOX FUNCTION

function openImg(src) {
  document.getElementById("lightbox").style.display = "flex";
  document.getElementById("lightbox-img").src = src;
}

function closeImg() {
  document.getElementById("lightbox").style.display = "none";
}
// COUNTER ANIMATION

const counters = document.querySelectorAll(".counter-box h3");

counters.forEach(counter=>{
let target = parseInt(counter.innerText);
let count = 0;

let update = ()=>{
count += Math.ceil(target/100);

if(count < target){
counter.innerText = count + "+";
requestAnimationFrame(update);
}else{
counter.innerText = target + "+";
}
};

update();

});
// NAVBAR SHADOW ON SCROLL

window.addEventListener("scroll",function(){

const header=document.querySelector("header");

if(window.scrollY>50){
header.style.boxShadow="0 5px 15px rgba(0,0,0,0.3)";
}else{
header.style.boxShadow="none";
}

});
// SCROLL ANIMATION

const faders=document.querySelectorAll("section");

window.addEventListener("scroll",()=>{

faders.forEach(el=>{

const top=el.getBoundingClientRect().top;

if(top<window.innerHeight-100){
el.classList.add("show");
}

});

});
// PAGE LOADER FIX

window.addEventListener("load", function () {
  const loader = document.getElementById("loader");
  loader.style.opacity = "0";
setTimeout(()=>{
  loader.style.display = "none";
},500);
});
// ADMIN POPUP

function openAdmin(){
document.getElementById("adminPopup").classList.add("show");
}

function closeAdmin(){
document.getElementById("adminPopup").classList.remove("show");
}


// LOGIN DROPDOWN

const loginBtn = document.getElementById("loginBtn");
const loginMenu = document.getElementById("loginMenu");

// ADMIN LOGIN CLICK

const adminLogin = document.getElementById("adminLogin");

adminLogin.addEventListener("click", function(e){
e.preventDefault();
openAdmin();
});
window.onclick = function(e){

const adminPopup = document.getElementById("adminPopup");
const teacherPopup = document.getElementById("teacherPopup");
const studentPopup = document.getElementById("studentPopup");
const admissionPopup = document.getElementById("admissionPopup");

if(e.target === adminPopup){
adminPopup.classList.remove("show");
}

if(e.target === teacherPopup){
teacherPopup.classList.remove("show");
}

if(e.target === studentPopup){
studentPopup.classList.remove("show");
}

if(e.target === admissionPopup){
admissionPopup.classList.remove("show");
}

};
// ======================= ADMISSION FORM POPUP =======================
document.addEventListener("DOMContentLoaded", function () {

  const admissionForm = document.getElementById("admissionForm");
  const admissionPopup = document.getElementById("admissionPopup");
  const admissionBtn = document.getElementById("admissionBtn");
  const topMsg = document.getElementById("topSuccess");
  const successMsg = document.getElementById("successMsg");

  function resetPreviews() {
    const photoPreview = document.getElementById("photoPreview");
    if(photoPreview) photoPreview.style.display = "none";
  }

  // OPEN POPUP
  function openAdmission() {
    admissionPopup.classList.add("show");
    if(admissionForm) admissionForm.reset();
    if(successMsg) successMsg.style.display = "none";
    if(topMsg) topMsg.classList.remove("show");
    resetPreviews();
  }

  // CLOSE POPUP
  function closeAdmission() { admissionPopup.classList.remove("show"); }

  // Global functions
  window.openAdmission = openAdmission;
  window.closeAdmission = closeAdmission;

  // Navbar / Apply Now button
  if(admissionBtn){
    admissionBtn.addEventListener("click", function(e){
      e.preventDefault();
      openAdmission();
    });
  }

  // FORM SUBMIT
  if(admissionForm){
    admissionForm.addEventListener("submit", function(e){
      e.preventDefault();

      // VALIDATION
      const email = document.getElementById("email").value;
      const mobile = document.getElementById("mobile").value;
      const fatherMobile = document.getElementById("fatherMobile").value;
      const aadhar = document.getElementById("aadhar_number").value;
      const emailRegex = /^\S+@\S+\.\S+$/;
      const mobileRegex = /^\d{10}$/;

      if(email && !emailRegex.test(email)) { alert("Enter valid email"); return; }
      if(mobile && !mobileRegex.test(mobile)) { alert("Enter 10-digit mobile"); return; }
      if(fatherMobile && !mobileRegex.test(fatherMobile)) { alert("Enter 10-digit parent mobile"); return; }
      if(aadhar && !/^\d{12}$/.test(aadhar)) { alert("Enter 12-digit Aadhar"); return; }

      // SHOW SUCCESS MSG
      if(topMsg){ topMsg.classList.add("show"); setTimeout(() => topMsg.classList.remove("show"), 3000); }
      if(successMsg) successMsg.style.display = "block";

      // CLOSE POPUP & RESET FORM AFTER 3 SECONDS
      setTimeout(() => {
        admissionForm.reset();
        closeAdmission();
        if(successMsg) successMsg.style.display = "none";
        resetPreviews();
      }, 3000);
    });
  }

  // PHOTO PREVIEW
  const photoInput = document.getElementById("photo");
  const photoPreview = document.getElementById("photoPreview");

  if(photoInput && photoPreview){
    photoInput.addEventListener("change", function(){
      const file = this.files[0];
      if(file){
        const reader = new FileReader();
        reader.onload = function(e){
          photoPreview.src = e.target.result;
          photoPreview.style.display = "block";
        }
        reader.readAsDataURL(file);
      }
    });
  }

});

function generateStudentID(){

let year = new Date().getFullYear();

let random = Math.floor(1000 + Math.random() * 9000);

let id = "STU" + year + random;

document.getElementById("studentID").value = id;

}

window.addEventListener("load", generateStudentID);
document.addEventListener("click", function(e){
  if(!loginBtn.contains(e.target) && !loginMenu.contains(e.target)){
    loginMenu.classList.remove("show");
  }
});
document.addEventListener("click", function(e){
  if(!nav.contains(e.target) && !toggle.contains(e.target)){
    nav.classList.remove("active");
  }
});


document.addEventListener("DOMContentLoaded", function () {

  const admissionPopup = document.getElementById("admissionPopup");
  const admissionBtn = document.getElementById("admissionBtn");

  // OPEN POPUP
  function openAdmission() {
    admissionPopup.classList.add("show");
  }

  // CLOSE POPUP
  function closeAdmission() {
    admissionPopup.classList.remove("show");
  }

  // NAVBAR BUTTON CLICK
  if (admissionBtn) {
    admissionBtn.addEventListener("click", function (e) {
      e.preventDefault();
      openAdmission();
    });
  }


  window.openAdmission = openAdmission;
  window.closeAdmission = closeAdmission;

});
document.addEventListener("DOMContentLoaded", function () {

  const admissionPopup = document.getElementById("admissionPopup");
  const admissionBtn = document.getElementById("admissionBtn");

  // OPEN POPUP
  function openAdmission() {
  document.getElementById("admissionPopup").classList.add("show");

  // 🔥 message hide kar do
  const successMsg = document.getElementById("successMsg");
  if (successMsg) {
    successMsg.style.display = "none";
  }
}

  // CLOSE POPUP
  function closeAdmission() {
    admissionPopup.classList.remove("show");
  }

  // NAVBAR BUTTON CLICK
  if (admissionBtn) {
    admissionBtn.addEventListener("click", function (e) {
      e.preventDefault();
      openAdmission();
    });
  }


  window.openAdmission = openAdmission;
  window.closeAdmission = closeAdmission;

});