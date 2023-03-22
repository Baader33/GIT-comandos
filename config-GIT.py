
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

        SERVER

#Cloud Services como github/gitlab. En genearl servidores remotos
#Se emplean comandos como git push que carga contenido de un repositorio local a uno 
#remoto


