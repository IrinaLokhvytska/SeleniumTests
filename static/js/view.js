Vue.component('todo-item', {
    props: ['title'],
    template: `
    <li class="list-group-item">
        <button v-on:click="$emit('remove')" class="btn btn-dark">Remove</button>
        {% raw %}{{title}}{% endraw %}
    </li>
  `
});

new Vue({
  el: '#todo-list-example',
  data: {
    newTodoText: '',
    todos: [
      {
        id: 1,
        title: 'Run the project',
      },
      {
        id: 2,
        title: 'Start Selenium Tests',
      },
      {
        id: 3,
        title: 'Enjoy'
      }
    ],
    nextTodoId: 4
  },
  methods: {
    addNewTodo: function () {
      this.todos.push({
        id: this.nextTodoId++,
        title: this.newTodoText
      });
      this.newTodoText = ''
    }
  }
});
