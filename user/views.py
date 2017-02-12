from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# for the class 'SignUpView'
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy

from tictactoe.models import Game, Move, Invitation 


@login_required
def home(request):
    my_games = Game.objects.games_for_user(request.user)
    active_games = my_games.filter(status="A")
    finished_games = my_games.exclude(status="A")
    waiting_games = active_games.filter(next_to_move=request.user)
    other_games = active_games.exclude(next_to_move=request.user)
    invitations = request.user.invitations_received.all()
    context = {'other_games': other_games,
                'waiting_games': waiting_games,
                'finished_games': finished_games,
                'invitations': invitations}
    return render(request, "user/home.html", context)

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "user/signup.html"
    success_url = reverse_lazy('user_home')

'''
We can create views with common functionality with almost no code when we make use of django generic views.
Some examples would be:
    - TemplateView  let you show a template;
    - DetailView    will retrieve a single object from the database and show it to the user.;
    - ListView      will do the same for a list of Model objects;

there is also the generic form-editing views that will generating a form and logic for a model class.
Generic Form editing views:
    - CreateView    let you create a new instance of your model
    - UpdateView    will edit a model instance
    - DeleteView    will remove an instance.

in order to know more about the topic 'generic views' go to:
    http://goo.gl/h2ZC3k
'''