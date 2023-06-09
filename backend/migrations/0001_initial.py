# Generated by Django 4.2.1 on 2023-05-13 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('idCliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombreCliente', models.CharField(max_length=100)),
                ('nombreUsuario', models.CharField(max_length=50, unique=True)),
                ('telefono', models.CharField(max_length=12)),
                ('contraseña', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('idComuna', models.AutoField(primary_key=True, serialize=False)),
                ('nombreComuna', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Consola',
            fields=[
                ('idConsola', models.AutoField(primary_key=True, serialize=False)),
                ('nombreConsola', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('idDireccion', models.AutoField(primary_key=True, serialize=False)),
                ('nombreCalle', models.CharField(max_length=50)),
                ('numeroCasa', models.IntegerField()),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('idEmpleado', models.AutoField(primary_key=True, serialize=False)),
                ('nombreEmpleado', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EstadoVenta',
            fields=[
                ('idEstadoVenta', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('idGenero', models.AutoField(primary_key=True, serialize=False)),
                ('nombreGenero', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MetodoPago',
            fields=[
                ('idMetodoPago', models.AutoField(primary_key=True, serialize=False)),
                ('tipoMetodo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('idRegion', models.AutoField(primary_key=True, serialize=False)),
                ('nombreRegion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('idRol', models.AutoField(primary_key=True, serialize=False)),
                ('nombreRol', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('idVenta', models.AutoField(primary_key=True, serialize=False)),
                ('totalPago', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.cliente')),
                ('estadoVenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.estadoventa')),
                ('metodoPago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.metodopago')),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('idSucursal', models.AutoField(primary_key=True, serialize=False)),
                ('direccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.direccion')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.AutoField(primary_key=True, serialize=False)),
                ('stock', models.IntegerField(default=0)),
                ('nombreProducto', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8)),
                ('imagen', models.ImageField(upload_to='')),
                ('consola', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.consola')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.genero')),
            ],
        ),
        migrations.CreateModel(
            name='Guia_despacho_detalle',
            fields=[
                ('idGuiaDespacho_detalle', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=6)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Guia_despacho',
            fields=[
                ('idGuiaDespacho', models.AutoField(primary_key=True, serialize=False)),
                ('fechaEmision', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.cliente')),
                ('despachador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.empleado')),
                ('guia_despacho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.guia_despacho_detalle')),
            ],
        ),
        migrations.AddField(
            model_name='empleado',
            name='rol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.rol'),
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('idDetalleVenta', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.producto')),
                ('venta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.venta')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_bodega',
            fields=[
                ('idDetalleBodega', models.AutoField(primary_key=True, serialize=False)),
                ('cantidadProd', models.DecimalField(decimal_places=2, max_digits=6)),
                ('lugarProd', models.CharField(max_length=100)),
                ('bodegaa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.consola')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='direccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.direccion'),
        ),
        migrations.CreateModel(
            name='Bodega',
            fields=[
                ('idBodega', models.AutoField(primary_key=True, serialize=False)),
                ('direccionbodega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.direccion')),
            ],
        ),
    ]
