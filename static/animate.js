const canvas = document.getElementById("canvas")
const ctx = canvas.getContext("2d")

let pixels = []


document.getElementById("upload").onchange = async function () {

    const file = this.files[0]
    if (!file) return

    // Visa originalbild
    const img = new Image()
    const url = URL.createObjectURL(file)
    img.src = url

    img.onload = () => {

        // Rensa canvas och rita originalbild
        ctx.clearRect(0, 0, canvas.width, canvas.height)
        ctx.drawImage(img, 0, 0, canvas.width, canvas.height)

        // Släpp URL-resursen
        URL.revokeObjectURL(url)
    }

    // Skicka till backend
    const form = new FormData()
    form.append("image", file)

    const res = await fetch("/process", {
        method: "POST",
        body: form
    })

    pixels = await res.json()

    // Vänta så man hinner se bilden
    setTimeout(startAnimation, 2000)
}

function startAnimation(){

    let t = 0

    function frame(){

        ctx.clearRect(0,0,canvas.width,canvas.height)

        pixels.forEach(p => {

            let x = p.x0 + t*(p.x1 - p.x0)
            let y = p.y0 + t*(p.y1 - p.y0)

            ctx.fillStyle = `rgb(${p.color[2]},${p.color[1]},${p.color[0]})`
            ctx.fillRect(x,y,1,1)

        })

        t += 0.02

        if(t < 1){
            requestAnimationFrame(frame)
        }
    }

    frame()
}