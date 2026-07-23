document.addEventListener("DOMContentLoaded", () => {

    const modalElement = document.getElementById("modalGaleria");

    if (!modalElement) return;

    const modal = new bootstrap.Modal(modalElement);

    const contenidoGaleria = document.getElementById("contenidoGaleria");
    const tituloGaleria = document.getElementById("tituloGaleria");

    document.querySelectorAll(".btn-galeria").forEach(boton => {

        boton.addEventListener("click", async () => {

            const galeriaId = boton.dataset.id;
            const titulo = boton.dataset.titulo;

            tituloGaleria.textContent = titulo;

            contenidoGaleria.innerHTML = `
                <div class="col-12 text-center py-5">

                    <div class="spinner-border text-success" role="status">

                        <span class="visually-hidden">
                            Cargando...
                        </span>

                    </div>

                    <p class="mt-3">
                        Cargando imágenes...
                    </p>

                </div>
            `;

            modal.show();

            try {

                const response = await fetch(`/galeria/${galeriaId}/imagenes`);

                if (!response.ok) {
                    throw new Error("No se pudieron obtener las imágenes.");
                }

                const imagenes = await response.json();

                contenidoGaleria.innerHTML = "";

                if (imagenes.length === 0) {

                    contenidoGaleria.innerHTML = `
                        <div class="col-12">

                            <div class="alert alert-info text-center">

                                Esta galería no tiene imágenes.

                            </div>

                        </div>
                    `;

                    return;

                }

                imagenes.forEach(imagen => {

                    contenidoGaleria.innerHTML += `

                        <div class="col-lg-4 col-md-6">

                            <div class="card h-100 shadow-sm">

                                <img
                                    src="/static/uploads/galeria_imagenes/${imagen.ruta_imagen}"
                                    class="card-img-top img-galeria"
                                    data-src="/static/uploads/galeria_imagenes/${imagen.ruta_imagen}"
                                    alt="${imagen.descripcion ?? ''}"
                                    style="height:250px; object-fit:cover; cursor:pointer;">

                                <div class="card-body">

                                    <p class="text-center mb-0">

                                        ${imagen.descripcion ?? ""}

                                    </p>

                                </div>

                            </div>

                        </div>

                    `;

                });

            }
            catch (error) {

                console.error(error);

                contenidoGaleria.innerHTML = `
                    <div class="col-12">

                        <div class="alert alert-danger text-center">

                            Ocurrió un error al cargar la galería.

                        </div>

                    </div>
                `;

            }

        });

    });

});