// study_fieldsの動作

// 学習分野の新しい行の追加
const addRowFields = (btn) => {
  const tableBody = document.querySelector("#study-fields tbody");
  const newRow = document.createElement("tr");
  newRow.classList.add("study-tr", "fields");
  newRow.innerHTML = `
    <td class="table-num"></td>
    <td class="table-fieldname"><input type="text" name="fieldname[]" value=""></td>
    <td class="table-field-color"><input type="color" name="color_code[]" value="#000000"></td>
    <td class="table-delete">
    <input type="hidden" name="field_id[]" value="">
    <input type="hidden" name="row_action[]" value="new">
    <button class="delete-button" type="button" onclick="removeRow(this)">🗑️</button>
    </td>`;
  tableBody.appendChild(newRow);

  // 追加後に番号を振り直す
  renumberRows();
};

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
