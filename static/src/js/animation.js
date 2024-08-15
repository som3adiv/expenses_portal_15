// document.addEventListener('DOMContentLoaded', function() {
//             // Get all the value elements and rectangles
//             const values = [
//                 { element: document.querySelector('.value1'), rectangle: document.querySelector('.rectangle-copy') },
//                 { element: document.querySelector('.value2'), rectangle: document.querySelector('.rectangle-copy1') },
//                 { element: document.querySelector('.value3'), rectangle: document.querySelector('.rectangle-copy2') },
//                 { element: document.querySelector('.value4'), rectangle: document.querySelector('.rectangle-copy3') },
//                 { element: document.querySelector('.value5'), rectangle: document.querySelector('.rectangle-copy4') }
//             ];

//             // Calculate total value
//             const totalValue = values.reduce((total, item) => {
//                 if (item.element) {
//                     return total + parseFloat(item.element.dataset.value);
//                 }
//                 return total;
//             }, 0);

//             if (totalValue === 0) {
//                 console.error('Total value is zero or not calculated correctly.');
//                 return;
//             }

//             // Set the width of each rectangle based on its value
//             values.forEach(item => {
//                 if (item.element && item.rectangle) {
//                     const percentage = (parseFloat(item.element.dataset.value) / totalValue) * 100;
//                     item.rectangle.style.width = percentage + '%';
//                 } else {
//                     console.error('Element or rectangle not found for', item);
//                 }
//             });
//         });