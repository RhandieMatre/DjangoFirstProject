from django.http import HttpResponse


def index (request):
    return HttpResponse("<h1>Hello! Welcome to my Site!</h1><hr></hr> <h3>'/mission' & '/vision' & '/objectives'</h3>")

def mission (request):
    return HttpResponse("<center><h1>Mission</h1></center><hr> </hr><center><p>The College of Computing and Multimedia Studies<br>shall produce competent and innovative professionals<br>or Technopreneurs in the Information and Communication Technology (ICT)<br>industry adequately prepared in the practice of their profession<br>supportive of national development goals and standards of global excellence.</p></center>")

def vision (request):
    return HttpResponse("<center><h1>Vision</h1></center><hr> </hr><center><p>The College of Computing and Multimedia Studies<br>shall be a center of excellence in delivering<br>Computing and Multimedia education</p></center>")
def objectives (request):
    return HttpResponse("<center><h1>Objectives</h1></center> <hr> </hr> <center><p>After graduation, alumini of MSEUF-CCMS programs shall:<br>1. Be employed and demonstrate professionalism, competence and passion in solving contemporary computing problems by developing or utilizing innovative IT solutions;<br>2. Embark in lifelong learning or reaserch to attune to the continous innovation in the IT industry in order to adapt the changing demands of the global market; and<br>3. Exhibit leadership and teamwork, and commitment to the respective local or global organizations.</p></center>")

