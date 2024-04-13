function calculateTax() {
  // Get references to input fields
  const incomeInput = document.getElementById('income');
  const extraIncomeInput = document.getElementById('extra-income');
  const deductionsInput = document.getElementById('deductions');
  const ageInput = document.getElementById('age');
  const tooltip = document.getElementById('tooltipText');
  const questionMark = document.getElementById('question');

  // Check if input fields exist
  if (!incomeInput || !extraIncomeInput || !deductionsInput) {
    console.error("Input fields not found");
    return;
  }
  // Parse input values
  const income = parseFloat(incomeInput.value);
  const extraIncome = parseFloat(extraIncomeInput.value) || 0;
  const deductions = parseFloat(deductionsInput.value) || 0;
  const age = parseInt(ageInput.value);
  // let age;
  // let taxRate;


  

  
  // Calculate total income (after deductions)
  const totalIncome = income + extraIncome - deductions;

  // Calculate taxable income above 8 Lakhs
  const taxableAmount = Math.max(totalIncome - 800000, 0);
  let taxRate;

  // Determine tax rate based on age
  if (age < 40) {
    taxRate = 0.3;
  } else if (age >= 40 && age < 60) {
    taxRate = 0.4;
  } else if (age >= 60) {
    taxRate = 0.1;
  } else {
    questionMark.style.display   = "flex"
    questionMark.addEventListener("mouseenter",function (){
      tooltip.style.display = "block"
    })
    questionMark.addEventListener("mouseleave",function(){
      tooltip.style.display = "none"
    })
   

;

}
  const taxAmount = taxableAmount * taxRate;

  // Display results in modal
  const modal = document.getElementById('modal');
  modal.style.display = 'block';
  document.getElementById('tax-amount').textContent = `After Deductions: ₹${taxAmount.toFixed(2)}`;

  // Close modal functionality
  const closeModalBtn = document.getElementById('close-modal');
  closeModalBtn.addEventListener('click', () => {
    modal.style.display = 'none';
  });
}

// Event listener for submit button
const submitButton = document.getElementById('submit');
submitButton.addEventListener("click", calculateTax);
