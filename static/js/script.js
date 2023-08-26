function showReplyForm(commentary) {
  const hiddenIdElement = commentary.querySelector('.hidden.id');
  const parentInput = document.querySelector('[name="parent_id"]');
  const replyFlag = document.querySelector('.reply_flag');
  const cancelButton = document.querySelector('.data-reply-form');
  const commentText = commentary.textContent;

  if (hiddenIdElement) {
      const hiddenId = hiddenIdElement.textContent;
      parentInput.value = hiddenId;
      replyFlag.textContent = commentText;
      replyFlag.style.display = 'block';
      cancelButton.style.display = 'block';
  } else {
      parentInput.value = '';
      replyFlag.style.display = 'none';
      cancelButton.style.display = 'none';
  }
}
function cancelReply(cancelButton) {
  const replyFlag = document.querySelector('.reply_flag');
  const parentInput = document.querySelector('[name="parent_id"]');
  replyFlag.textContent = '';
  parentInput.value = '';
  cancelButton.style.display = 'none';
}


function showComments(triggerElement) {
  var commentBars = document.querySelectorAll('.commentbar');
  commentBars.forEach(function(commentBar) {
    commentBar.style.display = 'none';
  });

  var commentIcon = triggerElement.querySelector('.comment-icon');
  var closeIcon = triggerElement.querySelector('.close-icon');

  if (commentIcon.classList.contains('hidden')) {
    commentIcon.classList.remove('hidden');
    closeIcon.classList.add('hidden');
    var commentBar = triggerElement.closest('.threaders').querySelector('.commentbar');
    commentBar.style.display = 'none';
  } else {
    commentIcon.classList.add('hidden');
    closeIcon.classList.remove('hidden');
    var commentBar = triggerElement.closest('.threaders').querySelector('.commentbar');
    commentBar.style.display = 'block';
  }
}

function upvoteThread(thread_id) {
    fetch(`/upvote/${thread_id}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(() => {
       
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
function downvoteThread(thread_id) {
  fetch(`/downvote/${thread_id}`, {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      }
  })
  .then(() => {
     
  })
  .catch(error => {
      console.error('Error:', error);
  });
}
