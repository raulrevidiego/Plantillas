#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <fstream>
#include <stdexcept>
using namespace std;

// VARIABLES Y TIPOS BÁSICOS
int    entero = <número>;           // Número entero
float  decimal = <número>.<dec>f;    // Decimal simple precisión
double precio = <número>.<dec>;     // Decimal doble precisión
char   letra = '<carácter>';       // Un solo carácter
bool   activo = true;               // true o false
string nombre = "<texto>";          // Cadena de texto


// CONSTANTES
const int MAX = <valor>;              // No puede cambiar tras definirse


// ARRAYS  (tamaño fijo)
int arr[<N>] = { <v1>, <v2>, <v3> };   // Array de N enteros
arr[0];                               // Acceso por índice (empieza en 0)


// VECTOR  (array dinámico, tamaño variable)
vector << tipo >> v = { <v1>, <v2> };
v.push_back(<valor>);                 // Añade al final
v.pop_back();                         // Elimina el último
v[0];                                 // Acceso por índice
v.size();                             // Número de elementos
v.empty();                            // true si está vacío


// MAP  (pares clave-valor, ordenado por clave)
map << tipo_clave > , <tipo_valor >> m;
m["<clave>"] = <valor>;               // Insertar / actualizar
m.at("<clave>");                      // Leer (lanza excepción si no existe)
m.count("<clave>");                   // 1 si existe, 0 si no
m.erase("<clave>");                   // Eliminar una clave


// CONDICIONALES
if (<condición>) {
    // Código si true
}
else if (<otra_condición>) {
    // Código si la segunda condición es true
}
else {
    // Código si ninguna se cumple
}
// Operadores: ==  !=  >  <  >=  <=  &&  ||  !

// TERNARIO  (condición compacta en una línea)
<tipo> var = (<condición>) ? <valor_true> : <valor_false>;


// BUCLES
for (int i = 0; i < <N>; i++) {       // Recorre de 0 a N-1
    // Usa i como índice
}

for (auto& <elem> : <vector>) {        // Recorre cada elemento del vector
    // Usa <elem> directamente (& evita copiar)
}

while (<condición>) {
    // Repite mientras la condición sea true
    // break    → sale del bucle
    // continue → salta a la siguiente iteración
}


// FUNCIONES
<tipo_retorno> <nombreFuncion>(<tipo1> <param1>, <tipo2> <param2> = <defecto>) {
    // Lógica de la función
    return <resultado>;                // Omitir si el retorno es void
}

// Llamada
<nombreFuncion>(<valor1>);
<tipo_retorno> resultado = <nombreFuncion>(<valor1>, <valor2>);


// CLASES
class <NombreClase> {
public:
    <tipo> <atributo>;                 // Atributo público

    <NombreClase>(<tipo> <param>) {   // Constructor: se llama al crear el objeto
        this-><atributo> = <param>;
    }

    <tipo_retorno> <metodo>() {        // Método público
        return this-><atributo>;
    }

private:
    <tipo> <atributo_privado>;         // Solo accesible desde dentro de la clase
};

// Crear objeto
<NombreClase> obj(<valor>);
obj.<metodo>();                        // Llamar a un método


// PUNTEROS Y REFERENCIAS  (gestión de memoria)
int  x = 5;
int* ptr = &x;                       // ptr guarda la dirección de x
*ptr = 10;                       // Modifica x a través del puntero
int& ref = x;                        // ref es un alias de x (misma dirección)

int* arr = new int[<N>];             // Reserva memoria dinámica
delete[] arr;                          // ¡Siempre liberar la memoria reservada!


// MANEJO DE ERRORES
try {
    if (<condición_error>) throw runtime_error("<mensaje de error>");
    // Código que puede lanzar excepciones
}
catch (const runtime_error& e) {
    cerr << "Error: " << e.what() << endl;   // e.what() da el mensaje
}
catch (const exception& e) {
    cerr << "Excepción: " << e.what() << endl; // Captura cualquier std::exception
}
// Excepciones comunes: runtime_error, out_of_range, invalid_argument


// LECTURA Y ESCRITURA POR CONSOLA
cout << "<texto>" << endl;             // Imprimir en pantalla
cout << "Valor: " << <variable> << endl;
cin >> <variable>;                    // Leer un dato del teclado
getline(cin, <string_var>);            // Leer una línea completa (con espacios)


// ARCHIVOS
ifstream entrada("<ruta/archivo.txt>");  // Abrir para leer
if (entrada.is_open()) {
    string linea;
    while (getline(entrada, linea)) {
        cout << linea << endl;           // Procesa cada línea
    }
    entrada.close();
}

ofstream salida("<ruta/archivo.txt>");   // Abrir para escribir (sobreescribe)
// ofstream salida("<ruta>", ios::app); // ios::app para añadir al final
if (salida.is_open()) {
    salida << "<texto>" << endl;
    salida.close();
}


// STRINGS  (operaciones útiles)
string s = "<texto>";
s.length();                            // Longitud
s.substr(<inicio>, <longitud>);        // Subcadena
s.find("<subcadena>");                 // Posición (string::npos si no existe)
s.replace(<pos>, <longitud>, "<nuevo>"); // Reemplaza trozo
s += "<más texto>";                    // Concatenar
to_string(<número>);                   // Número → string
stoi("<123>");                         // String → int
stod("3.14");                          // String → double


// MAIN  (punto de entrada del programa)
int main() {
    // Tu código aquí
    return 0;                          // 0 = ejecución correcta
}