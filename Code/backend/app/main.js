fetch("https://www.wwimmo.ch/blog/rimo-r5/")
  .then(function (response) {
    // The API call was successful!
    return response.text();
  })
  .then(function (html) {
    // This is the HTML from our response as a text string
    console.log(html);
  })
  .catch(function (err) {
    // There was an error
    console.warn("Something went wrong.", err);
  });
