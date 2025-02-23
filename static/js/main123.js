function post_comment(){
    console.log("Commented")
    const modal = document.getElementById('postModal');
    const postid = document.getElementById("comment_id").getAttribute("postId");
        if (modal) {
            document.body.classList.add('modal-open');
            modal.classList.remove('hidden');
            modal.classList.add('flex');
           let authorName = document.getElementById("authorName").value;
            let commentText = document.getElementById("commentText").value;
            let title = document.querySelector("#h2_title").textContent;
            console.log(authorName, commentText);
            fetch("https://basic-blog.teamrabbil.com/api/create-comment", {
                body: JSON.stringify({ "list_id": postid,
                    "author": authorName,
                    "comment": commentText
                 }),
                headers: {
                    "Content-Type": "application/json"
                },
                method: "POST"
              }).then(response => response.json())
              .then(data => {
                console.log(data);
                openModal(postid, title);
                document.getElementById("authorName").value= " ";
                document.getElementById("commentText").value = " ";
                setTimeout(() => {
                    closeModal();
                }, 2000);
              });
                
            
        };
        
};



// Modal functions
function openModal(id, title) {
    console.log(id);
    console.log(title);
    const modal = document.getElementById('postModal');
      
        if (modal) {
            document.body.classList.add('modal-open');
            modal.classList.remove('hidden');
            modal.classList.add('flex');

            fetch(
                `https://basic-blog.teamrabbil.com/api/post-details/${id}`
            ).then(response => response.json())
                .then(data => {
            document.querySelector("#h2_title").textContent = title;
            document.querySelector('#postImage').setAttribute('src', data.postDetails.img);
            document.querySelector("#post_content").textContent = data.postDetails.content;
             console.log(data.postDetails);
             document.getElementById("comment_id").setAttribute("postId", id);
             document.querySelector('#post_comments').innerHTML =" ";
            data.postComments.forEach(el => {
                const dateString = el.created_at;

                 // Convert the string to a Date object
                 const date = new Date(dateString);

                 // Format the date
                 const options = { minute: '2-digit', hour:'2-digit', day: '2-digit', month: 'long', year: 'numeric' };
                 const formattedDate = date.toLocaleDateString('en-US', options);

                console.log(formattedDate); // Output: "28 December, 2024"
                document.querySelector('#post_comments').innerHTML +=`
                
                 <div class="bg-white p-6 rounded-xl shadow-sm border border-gray-100">
                            <div class="flex items-center gap-3 mb-3">
                                <div
                                    class="w-10 h-10 rounded-full bg-purple-100 flex items-center justify-center text-purple-600 font-semibold">
                                    ${el.author[0].toUpperCase()}
                                </div>
                                <div>
                                    <div class="font-semibold text-gray-800"> ${el.author}</div>
                                    <div class="text-sm text-gray-500">${formattedDate}</div>
                                </div>
                            </div>
                            <p class="text-gray-600 leading-relaxed">${el.comment}</p>
                        </div>
                `;
            });
                    });
    };
   
};


function closeModal() {
    const modal = document.getElementById('postModal');
    if (modal) {
        modal.classList.remove('flex');
        modal.classList.add('hidden');
        document.body.classList.remove('modal-open');
    }
}

// Close modal when clicking outside
document.getElementById('postModal')?.addEventListener('click', function (e) {
    if (e.target === this) {
        closeModal();
    }
});

// Create a new buttons
const newButtons = document.querySelector("#buttons_container");

/*
catagories = [ "Technology", "Travel", "Design","Culture","Business"]
catagories.forEach(el => {
    newButtons.innerHTML +=`<button
    class="px-4 py-2 rounded-xl bg-gray-100 text-gray-600 hover:bg-purple-600 hover:text-white hover:shadow-lg hover:shadow-purple-200 transition-all text-sm sm:text-base whitespace-nowrap">
    ${el}
</button>`

});
*/

fetch( 
    'https://basic-blog.teamrabbil.com/api/post-categories'
).then((response) =>response.json())
 .then((data)=>{
   data.forEach((el) => {
    newButtons.innerHTML +=`
    <button 
    onclick = "postsSelector(${el.id}, '${el.name}')"  class="px-4 py-2 rounded-xl bg-gray-100 text-gray-600 hover:bg-purple-600 hover:text-white hover:shadow-lg hover:shadow-purple-200 transition-all text-sm sm:text-base whitespace-nowrap">
    ${el.name}
</button>`

   });
 });

 const newestAritle = () => {
    const posts_container = document.querySelector("#posts_container");
    document.getElementById("articles_name").textContent = "Newest Articles";
    posts_container.innerHTML ="";
    fetch(
            'https://basic-blog.teamrabbil.com/api/post-newest'
        )
          .then((response) =>response.json())
          .then((data) => {
            console.log(data);
            data.forEach(el =>{
                const dateString = el.updated_at;

                 // Convert the string to a Date object
                 const date = new Date(dateString);

                 // Format the date
                 const options = { minute: '2-digit', hour:'2-digit', day: '2-digit', month: 'long', year: 'numeric' };
                 const formattedDate = date.toLocaleDateString('en-US', options);

                console.log(formattedDate); 
                posts_container.innerHTML +=
                `<article
                class="bg-white rounded-2xl shadow-sm hover:shadow-xl transition-all overflow-hidden group">
                 <div class="relative overflow-hidden">
                            <img src="${el.img}" alt="Post Title"
                                class="w-full h-56 object-cover transform group-hover:scale-105 transition-transform duration-300">
                            <div class="absolute top-4 left-4">
                                <span
                                    class="px-4 py-2 bg-white/90 backdrop-blur-sm rounded-lg text-purple-600 text-sm font-semibold">
                                    Home
                                </span>
                            </div>
                        </div>
                <div class="p-6">
                    <h3
                        class="text-xl font-bold text-gray-800 mb-3 group-hover:text-purple-600 transition-colors">
                       ${el.title}
                    </h3>
                    <h1> Hello Ariful </h1>
                    <p class="text-gray-600 mb-4 line-clamp-2">
                        ${el.short}
                    </p>
                    <div class="flex items-center justify-between">
                        <span class="text-sm text-gray-500">${formattedDate}</span>
                        <button onclick="openModal(${el.id}, '${el.title}')"
                            class="text-purple-600 hover:text-purple-700 font-medium inline-flex items-center gap-2 transition-colors">
                            Read more →
                        </button>
                    </div>
                </div>
            </article>`;

            });        
        });
 };


const postsSelector = (id, name) => {
        const posts_container = document.querySelector("#posts_container");
        document.getElementById("articles_name").textContent = `${name} Articles`;
        posts_container.innerHTML = "";
fetch(
    `https://basic-blog.teamrabbil.com/api/post-list/${id}`
        ) .then((response) =>response.json())
        .then(data => {
            data.forEach(el =>{
                const dateString = el.updated_at;

                 // Convert the string to a Date object
                 const date = new Date(dateString);

                 // Format the date
                 const options = { minute: '2-digit', hour:'2-digit', day: '2-digit', month: 'long', year: 'numeric' };
                 const formattedDate = date.toLocaleDateString('en-US', options);
               
               posts_container.innerHTML +=
               `<article
                        class="bg-white rounded-2xl shadow-sm hover:shadow-xl transition-all overflow-hidden group">
                        <div class="relative overflow-hidden">
                            <img src="${el.img}" alt="Post Title"
                                class="w-full h-56 object-cover transform group-hover:scale-105 transition-transform duration-300">
                            <div class="absolute top-4 left-4">
                                <span
                                    class="px-4 py-2 bg-white/90 backdrop-blur-sm rounded-lg text-purple-600 text-sm font-semibold">
                                    Home
                                </span>
                            </div>
                        </div>
                        <div class="p-6">
                            <h3
                                class="text-xl font-bold text-gray-800 mb-3 group-hover:text-purple-600 transition-colors">
                               ${el.title}
                            </h3>
                            <p class="text-gray-600 mb-4 line-clamp-2">
                                ${el.short}
                            </p>
                            <div class="flex items-center justify-between">
                                <span class="text-sm text-gray-500">${formattedDate}</span>
                                <button onclick="openModal(${el.id},'${el.title}')"
                                    class="text-purple-600 hover:text-purple-700 font-medium inline-flex items-center gap-2 transition-colors">
                                    Read more →
                                </button>
                            </div>
                        </div>
                    </article>`;
                    
            });
        });
     };


    newestAritle();