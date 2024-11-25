from django.shortcuts import HttpResponse

def task_create(request):
    html_response = """
      <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
   <h1>
    Yangi vazifa yaratish
   </h1> 

   <form>

    <label for="name">
        Vazifa nomi:
        <input type="text" id="name" name="name">
    </label>

    <br>
    <br>

    <label for="tavsif">
        Tavsifi:
        <input type="text" id="tavsif" name="tavsif">
    </label>

    <br><br>

    <label for="muddat">
        Muddati:
        <input type="date" id="muddat" name="muddat">
    </label>

    <br><br>

    <label for="level">
        Muhimlik darajasi:
        <select name="level" id="level">
            <option value="Past">Past</option>
            <option value="O'rta">O'rta</option>
            <option value="Yurqori">Yuqori</option>
        </select>
    </label>

    <br><br>

    <button type="button">Vazifani saqlash</button>

   </form>
</body>
</html>
        
    """
    return HttpResponse(html_response)