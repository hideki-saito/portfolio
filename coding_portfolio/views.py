from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from coding_portfolio.models import Project, Language, About, Slide_Image, Question_Answer


# TODO: Be able to show <code> or <pre> blocks as code in posts. - Need help with this!


################################################################################
#                                                                              #
#    Copyright (C) 2016  Areeb Beigh <areebbeigh@gmail.com>                    #
#                                                                              #
#    This program is free software: you can redistribute it and/or modify      #
#    it under the terms of the GNU General Public License as published by      #
#    the Free Software Foundation, either version 3 of the License, or         #
#    (at your option) any later version.                                       #
#                                                                              #
#    This program is distributed in the hope that it will be useful,           #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of            #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
#    GNU General Public License for more details.                              #
#                                                                              #
#    You should have received a copy of the GNU General Public License         #
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     #
#                                                                              #
################################################################################


def index(request):
    """ Index view, returns a list of recent projects in the context """
    # recent_projects = []
    # for i in range(0, 6):
    #     try:
    #         recent_projects.append(Project.objects.order_by('-publish_date')[i])
    #     except IndexError:
    #         break

    projects = Project.objects.all()
    slide_images = Slide_Image.objects.all()
    question_answers = Question_Answer.objects.all()
    languages = Language.objects.all()

    context = {
        'projects': projects,
        'slide_images': slide_images,
        'question_answers': question_answers,
        'languages': languages,
    }

    return render(request, 'index.html', context)




def project_detail(request, project_id):
    """ Returns view for individual project pages """
    project_object = get_object_or_404(Project, id=project_id)
    context = {
        'project': project_object,
    }
    return render(request, 'project_detail.html', context)

def about(request):
    """ About view """
    try:
        about = About.objects.get().description
    except:
        about = "No information here yet."

    return render(request, 'about_page.html', {'about': about})
