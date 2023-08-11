{% extends 'base.html' %}
{% block content %}
<h1>TicTac</h1>

<form method="POST">
    <div class="mb-3">
      <label for="text" class="form-label">TicTac</label>
      <input name="text" type="text" class="form-control" id="text" aria-describedby="emailHelp">
      <div id="tictac" class="form-text">We'll never share your email with anyone else.</div>
    </div>

    <div class="form-check">
        <input name="move" value="true" type="checkbox" class="form-check-input" id="exampleCheck1">
        <label class="form-check-label" for="exampleCheck1">Check me out</label>
      </div>

    <button name="submit" type="submit" class="btn btn-primary">TicTac</button>
  </form>

  {% for note in current_user.notes %}
  {{ note.move }}
  {% endfor %}

  <div class="container" id="main">
    <span id="turn">Tic Tac Toe</span>

    <div class="box" style="border-left: 0; border-top: 0" id="box1"></div>
    <div class="box" style="border-top: 0" id="box2"></div>
    <div class="box" style="border-top: 0; border-right: 0" id="box3"></div>
    <div class="box" style="border-left: 0" id="box4"></div>
    <div class="box" id="box5"></div>
    <div class="box" style="border-right: 0" id="box6"></div>
    <div class="box" style="border-left: 0; border-bottom: 0" id="box7"></div>
    <div class="box" style="border-bottom: 0" id="box8"></div>
    <div class="box" style="border-right: 0; border-bottom: 0" id="box9"></div>
  </div>

  <button class="btn btn-rounded" id="replay">Play Again</button>

  
{% endblock %}