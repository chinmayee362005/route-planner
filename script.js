function addTask() {
    const taskText = document.getElementById("taskInput").value;
  
    if (taskText === "") return;
  
    const li = document.createElement("li");
    li.textContent = taskText;
  
    // ✅ Done Button
    const doneBtn = document.createElement("button");
    doneBtn.textContent = "Done";
    doneBtn.onclick = () => {
      li.style.textDecoration = "line-through";
      li.style.color = "gray";
      doneBtn.disabled = true; // disable after marking
    };
  
    // ❌ Delete Button
    const delBtn = document.createElement("button");
    delBtn.textContent = "Delete";
    delBtn.onclick = () => li.remove();
  
    li.appendChild(doneBtn);
    li.appendChild(delBtn);
    document.getElementById("taskList").appendChild(li);
  
    document.getElementById("taskInput").value = "";
  }
  