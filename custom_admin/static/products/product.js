function showProductOptions(icon) {
    var productOptions = icon.nextElementSibling;
    productOptions.style.display = productOptions.style.display === 'none' ? 'block' : 'none';
}

function editProduct(productId) {
    // Implement your edit product logic here
    console.log('Edit product with ID:', productId);
}

function deleteProduct(productId) {
    // Implement your delete product logic here
    console.log('Delete product with ID:', productId);
}
