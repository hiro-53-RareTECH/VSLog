// study_fieldsの動作

// 番号の振り直し
const renumberRows = () => {
  const rows = document.querySelectorAll(
    "#study-fields tbody tr.study-tr.fields",
  );
  rows.forEach((row, index) => {
    const numCell = row.querySelector(".table-num");
    if (numCell) {
      numCell.textContent = index + 1;
    }
  });
};

// 初期の空白行表示
const DEFAULT_ROWS = 5;

const ensureDefaultBlankRows = () => {
  const tableBody = document.querySelector("#study-fields tbody");
  const template = document.getElementById("fields-template");

  const currentCount = tableBody.querySelectorAll("tr.study-tr.fields").length;
  const need = Math.max(0, DEFAULT_ROWS - currentCount);

  for (let i = 0; i < need; i++) {
    const clone = template.content.cloneNode(true);
    tableBody.appendChild(clone);
  }

  renumberRows();
};

ensureDefaultBlankRows();

// 学習分野の新しい行の追加
const addRowFields = (btn) => {
  const tableBody = document.querySelector("#study-fields tbody");
  const template = document.getElementById("fields-template");
  const clone = template.content.cloneNode(true);
  tableBody.appendChild(clone);

  // 追加後に番号を振り直す
  renumberRows();
};

// 既存行の削除
const markDeleted = (btn) => {
  const result = window.confirm(
    "本当に学習分野を削除しますか？\n削除した場合、関連する学習分野の学習記録がすべて削除されます！",
  );
  if (result) {
    const row = btn.closest("tr");
    row.querySelector('input[name="row_action[]"]').value = "delete";
    document.forms["study_fields_process"].submit();
  }
};
