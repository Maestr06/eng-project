let valueField = document.getElementById("value");
let ulgaField = document.getElementById("ulga");
let resultBox = document.getElementById("result");
let ppkField = document.getElementById("ppk");
let pitField = document.getElementById("pit0");
let miejscePracyField = document.getElementById("miejsce");
let ppkProcPracownikField = document.getElementById("pracownik_proc_ppk");
let ppkProcPracownikDiv = document.getElementById("pracownik_proc_ppk_div");
let ppkProcPracodawcaField = document.getElementById("pracodawca_proc_ppk");
let ppkProcPracodawcaDiv = document.getElementById("pracodawca_proc_ppk_div");

let emerytalne, podstawaPit, zaliczkaPit, netto;
let chorobowe, rentowe, zdrowotne, brutto;
let pracownik_proc_ppk, pracodawca_proc_ppk, pracownik_ppk, pracodawca_ppk;
const PIT_ZERO = 85528;
const PROC_CHOROBOWE = 2.45;
const PROC_EMERYTALNE = 9.76;
const PROC_RENTOWE = 1.5;

function przelicz() {
  let value = Number(valueField.value);
  let ulga = Number(ulgaField.value);
  miejsce_pracy = 250;
  let stawkaPit = 0.12;
  let ppk_proc_pracow;
  let ppk_pracow;
  let ppk_proc_pracod;
  let ppk_pracod;
  let brutto_z_ppk = value;
  let result;
  emerytalne =
    Math.round((PROC_EMERYTALNE * 0.01 * value + Number.EPSILON) * 100) / 100;
  chorobowe =
    Math.round((PROC_CHOROBOWE * 0.01 * value + Number.EPSILON) * 100) / 100;
  rentowe =
    Math.round((PROC_RENTOWE * 0.01 * value + Number.EPSILON) * 100) / 100;
  zdrowotne =
    Math.round(
      ((value - emerytalne - chorobowe - rentowe) * 0.09 + Number.EPSILON) * 100
    ) / 100;

  if (!miejscePracyField.checked) {
    miejsce_pracy = 300;
  }

  podstawaPit = Math.round(
    value - emerytalne - chorobowe - rentowe - miejsce_pracy
  );

  zaliczkaPit = Math.round(podstawaPit * stawkaPit - ulga);

  if (pitField.checked) {
    zaliczkaPit = 0;
  }

  if (ppkField.checked) {
    ppk_proc_pracow = ppkProcPracownikField.value;
    ppk_proc_pracod = ppkProcPracodawcaField.value;
    ppk_pracow = ppk_proc_pracow * 0.01 * value;
    ppk_pracod = ppk_proc_pracod * 0.01 * value;
    brutto_z_ppk = Number(value) + ppk_pracod;
    podstawaPit = Math.round(
      brutto_z_ppk - emerytalne - chorobowe - rentowe - miejsce_pracy
    );
    zaliczkaPit = Math.round(podstawaPit * stawkaPit - ulga);
    if (pitField.checked) {
      zaliczkaPit = 0;
    }
    value -= ppk_pracow;
  }
  // console.log(ppk_pracow, ppk_pracod);
  resultBox.innerHTML = "";

  if ("" == value) {
    return;
  }

  result = value - chorobowe - rentowe - emerytalne - zdrowotne - zaliczkaPit;

  resultBox.innerHTML = result.toFixed(2) + "zł";
  console.log(brutto_z_ppk, zaliczkaPit, podstawaPit);
}

valueField.onchange = function () {
  przelicz();
};

ulgaField.onchange = function () {
  przelicz();
};

ppkProcPracownikField.onchange = function () {
  przelicz();
};

ppkProcPracodawcaField.onchange = function () {
  przelicz();
};

pitField.onchange = function () {
  przelicz();
};

miejscePracyField.onchange = function () {
  przelicz();
};

ppkField.onchange = function () {
  if (!ppkField.checked) {
    hide(ppkProcPracownikDiv);
    hide(ppkProcPracodawcaDiv);
    // ppkProcPracownikDiv.style.display = "none";
    // ppkProcPracodawcaDiv.style.display = "none";
  } else {
    ppkProcPracownikDiv.style.display = "block";
    ppkProcPracodawcaDiv.style.display = "block";
  }
  przelicz();
};

function hide(field) {
  field.style.display = "none";
}
