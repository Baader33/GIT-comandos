
        CURSO COMPLETO EN https://www.youtube.com/watch?v=VdGzPZ31ts8&t=635s        

        COMANDOS PREVIOS DE CONFIGURACIÓN DE GIT

git --version #Visualización de la versión instalada
git config --global user.name "nombre del usuario"
git config --global user.email useremail@useremail.com #no es necesario comillas"
git config --global core.editor "code --wait" #"code --wait" elije el editor code VS por defecto. Es posible usar cualquier otro editor

git config --global -e #muestra el archivo de texto de los comandos

        COMANDO core.autocrlf

#Este comando proporciona un control sobre los caracteres especiales al realizar un salto 
#de línea

        git config --global core.autocrlf true #user windows    
        git config --global core.autocrlf input #user linux


        FLUJO DE TRABAJO CON GIT

        PC---------->stage------------->commit------------>server

        ETAPA PREVIA DE INICIALIZACIÓN

#Es necesario realizar el proceso de inicialización de git sobre el directorio en el que deseamos trabajar

        git init #Inicializa un repositorio vacío en el directorio local actual.
                 #Inmediatamente crea un subdirectorio oculto .git
        ls -a #Comando bash que muestra el listado de elementos en el directorio              #incluyendo los ocultos.

        STAGE

#Si se desean agregar, editar o eliminar archivos a un repositorio, será necesario
#ingresar en le estapa "stage". En esta etapa se listan y se preparan los cambios
#que se desean realizar en el repositorio

#Comandos como git add, describen esta estapa
    
        git add archivo.ext #agrega a la etapa stage el archivo.ext
        git add archivo1.ext archivo2.ext ... #agrega varios archivos
        git add *.ext       #agrega todos los archivos .ext
        git add .           #agrega todos los archivos
        git restore archivo.ext #descarta los cambios en el directorio de trabajo
                                #descarta los cambios que se han hecho en un archivo
                                #que está en la espera de agregarse a la etapa

#NOTA: los archivos en espera a listarse serán los que se muestren mediante el
#comando git status y son los mismos que estén en la carpeta del reposiorio local

        git rm --cached archivo.ext #para sacar del área de stage
        mv a.ext b.ext              #cambia de nombre del archivo sin agregar al stage 
                                    #el cambio
        git mv a.ext b.ext          #Realiza el cambio de nombre y agrega (add) a stage

        gitignore

#En el caso de no querer hacer commits a ciertos archivos presentes en el repositorio local
#será necesario crear un archivo .gitignore
        
#Se crea el archivo .gitignore y se agregan los archivos o las direcciones de carpetas



        COMMIT

#En la etapa de commit se agregan los archivos agregados o editados que se listaron
#en la etapa stage, asi como lo cambios especificos sobre los archivos. En commit
#estan los archivos definitivos que se desean cargar, agregar, editar o eliminar en el 
#repositorio que posteriormente iran al servidor o la nube.

        git commit -m "mensaje de commit" #agrega a la etapa de commit los cambios o los
                                          #archivos. -m para escribir el comentario del 
                                          #comit                       
        git comit #abre el editor de texto predeterminado para git para editar el 
                                          #nombre del nuevo comit
        git log   #muestra los commits realizados, fecha y datos del autor que los realizó
        git log --oneline #muestra el registro de cada commit con un respectivo hash

RAMAS-BRANCH

#Son líneas de evolución que registran y marcan los diferentes commits o cambios en un processo, como un historial. 

        git branch #muesstra la rama actual en uso
        git checkout -b name-brach #crea una nueva rama llamda name-branch si no existe.
        git checkout name-branch #se cambia a la rama name-branch
        cat archivo.ext #muestra el contenido del archivo en texto planio
        git merge rama-anterior #si se desea traer archivos o modificaciones a la rama actual                                #será necesario usar merge y traos cambios o archivos de rama-anterior

        SERVER

#Cloud Services como github/gitlab. En genearl servidores remotos
#Se emplean comandos como git push que carga contenido de un repositorio local a uno 
#remoto


