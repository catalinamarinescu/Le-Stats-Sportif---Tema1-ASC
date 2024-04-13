##### Marinescu Maria-Catalina 334CA
### TEMA1 - LE STATS SPORTIF

> In organizarea temei, am completat functiile existente in scheletul oferit
si pentru rezolvarea efectiva am creat functii corespunzatoare fiecarei 

> In clasa ThreadPool, am initializat structurile
de care am avut nevoie si am pornit thread-urile pentru rezolvarea task-urilor. 
De asemenea, am creat 2 functii: **add_job** ce adauga un job la coada de
job-uri si statusul job-ului este actualizat in "running"; 
**shutdown** ce are rolul de a opri executia.
> In clasa task_runner, in metoda **run**, se scot pe rand job-urile din coada,
sunt executate, iar rezultatul fiecarui job este scris in fisierul 
corespunzator din directorul results/. Dupa executia job-ului starea acestuia
se actualizeaza in "done", iar in caz de eroare in "error".

> Am salvat datele din fisierul "nutrition_activity_obesity_usa_subset.csv" 
intr-o variabila data_set cu ajutorul bibliotecii pandas. Ulterior,
pentru fiecare functie am abordat o rezolvare similara: am filtrat data_set-ul
dupa coloanele ce contin intrebarea corespunzatoare, dupa anii specificati si 
in functie de caz, dupa statul specificat; am folosit functia **group_by**
pentru a grupa datele dupa state si functia **mean** pentru a calcula media.
Valorile din data_set-ul rezultat au fost transformate in dicitionar si 
returnate,ulterior la executie acestea fiind transformate in format json.
In functiile unde se specifica un stat anume am verificat daca statul exista
pentru setul ce contine intrebarea corespunzatoare.
Pentru functiile **best5** si **worst5** am verificat in plus, daca 
intrebarea face parte din cele in care minimul/maximul este cel mai bun/rau,
iar in functie de aceasta am pastrat fie primele 5 elemente, fie ultimele.
Pentru functia **diff_from_mean** am facut o lista cu toate statele
iar pentru fiecare am calculat state_mean, urmand apoi sa se faca diferenta.

> Pentru fiecare request primit pentru functiile din data_ingestor am verificat
daca a fost trimis inainte un request de tipul "graceful_shutdown". In caz
ca a fost primit atunci se va returna json-ul cu formatul specificat. Altfel,
am adaugat job-ul(functia specifica din data_ingestor, argumentul 
primit(data) si job-id-ul) in coada si am incrementat job_counter-ul, punand
un lock pe acesta deoarece este o resursa partajata.
> Pentru **get_response** am verificat daca job-id-ul exista. Daca nu, se va
intoarce un json cu mesaj de eroare. Daca exista si job-ul corespunzator este
terminat se va intoarce un json cu statusul si rezultatul job-ului. Daca exista
si nu este terminat se va intoarce un json cu statusul job-ului.
> Pentru **graceful_shutdown** se apeleaza functia din ThreadPool ce seteaza
flagul event-ului pe true si se opresc thread-urile.
> Pentru **num_jobs** se returneaza lungimea cozii, iar daca aceasta e goala
se returneaza 0.
> Pentru **jobs** se returneaza un json cu dictionarul ce contine 
job-id_ul(key) si statusul(value).

> Din punctul meu de vedere, tema a fost foarte utila pentru a intelege cum
functioneaza server-ul si clientul, cum se fac reqest-urile 
de acest tip si cum se raspunde la ele. Consider ca am aprofundat mult mai bine
aceste notiuni ce aveau baze de la materii precedente. A fost interesanta
partea de Flask, o alta notiune noua, si lucrul cu thread-uri a fost de
asemenea un plus pentru a fixa notiunile deja cunoscute.

> Din punctul de vedere al implementarii, consider ca la partea de calcul putea 
exista o abordare mai organizata. 

> Resurse utilizate
- https://ocw.cs.pub.ro/courses/asc/laboratoare/02
- https://ocw.cs.pub.ro/courses/asc/laboratoare/03
- https://www.geeksforgeeks.org/python-pandas-dataframe/
- https://mobylab.docs.crescdi.pub.ro/docs/parallelAndDistributed/laboratory5/

> Toate functionalitatile din enunt sunt implementate(fara partea de logging
si unittesting).
