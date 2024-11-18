function addBook() {
    const title = $('#title').val();
    const author = $('#author').val();
    const year = $('#year').val();
    const genre = $('#genre').val();

    const newBook = { title: title, author: author, year: parseInt(year), genre: genre };

    $.ajax({
        url: '/books',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(newBook),
        success: function(book) {
            const newListItem = $('<li>').text(`${book.title} by ${book.author} (${book.year}) - Genre: ${book.genre}`);
            $('#books-list').append(newListItem);

            $('#add-book-form')[0].reset();
        },
        error: function() {
            alert("Failed to add the book. Please check the input data.");
        }
    });
}
