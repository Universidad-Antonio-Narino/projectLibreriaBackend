# Libreria uan

Este proyecto es un proyecto universitaro, de la materia de diseño de bases de datos, el cual busqueda la practica de los conocimientos dados en la materia con el lenguaje sql, en el taller practico se podia hacer el codigo con solo sql y un conector de bases de datos para tres lenguajes, los cuales eran: java, c++ y python, en el momento el taller estaba desarrollado para un grupo de 6 estudiantes, el proyecto lo puede encontrar aqui([Exolicacion proyecto, titulado Libreria proyectos](/Libreria.md))

## 🛠 Skills
- [![Django][Django-logo]][Django-url]
- [![Python][Python-logo]][Python-url]
- [![HTML][HTML-logo]][HTML-url]
- [![CSS][CSS-logo]][CSS-url]
- [![JavaScript][JavaScript-logo]][JavaScript-url]
- [![MySQL][MySQL-logo]][MySQL-url]

[MySQL-logo]: https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white
[MySQL-url]: https://www.mysql.com/

[JavaScript-logo]: https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black
[JavaScript-url]: https://developer.mozilla.org/en-US/docs/Web/JavaScript

[CSS-logo]: https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white
[CSS-url]: https://developer.mozilla.org/en-US/docs/Web/CSS

[HTML-logo]: https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white
[HTML-url]: https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5

[Django-logo]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white
[Python-logo]: https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54

[Django-url]: https://www.djangoproject.com/
[Python-url]: https://www.python.org/


## Authors

- [@octokatherine](https://www.github.com/octokatherine)

## Features

- Light/dark mode toggle
- Live previews
- Fullscreen mode
- Cross platform

## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.