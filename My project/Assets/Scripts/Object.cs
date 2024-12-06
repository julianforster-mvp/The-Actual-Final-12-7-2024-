using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.InputSystem;
using TMPro;
using UnityEngine.SceneManagement;  // Import Scene Management


public class Object : MonoBehaviour
{
    public float speed = 0; 
    public TextMeshProUGUI countText;
    public GameObject winTextObject;
    private Rigidbody rb; 
    private int count;
    private float movementX;
    private float movementY;
   

    // Start is called before the first frame update
    void Start()
    {
        rb = GetComponent <Rigidbody>(); 
    
        count = 0; 
        SetCountText();
        winTextObject.SetActive(false);
    
    }

     
    private void FixedUpdate() 
    {
        Vector3 movement = new Vector3 (movementX, 0.0f, movementY);
        
        rb.AddForce(movement * speed); 

        transform.position += movement * speed * Time.deltaTime;
    }

    private void OnCollisionEnter(Collision collision)
    {
        if (collision.gameObject.CompareTag("Enemy"))
        {
            // Destroy the current object
            Destroy(gameObject); 
            // Update the winText to display "You Lose!"
            winTextObject.gameObject.SetActive(true);
            winTextObject.GetComponent<TextMeshProUGUI>().text = "You Lose!";
        }
    }



    
    void OnTriggerEnter(Collider other) 
    {
        
        if (other.gameObject.CompareTag("PickUp")) 
        {
            other.gameObject.SetActive(false);
            count = count + 1;

            SetCountText();
        }
        
       
    }
    
    
    
    void OnMove (InputValue movementValue)
    {
        Vector2 movementVector = movementValue.Get<Vector2>(); 

        movementX = movementVector.x; 
        movementY = movementVector.y; 
    }

    void SetCountText() 
    {
       countText.text =  "Count: " + count.ToString();
        if (count >= 4)
        {
           winTextObject.SetActive(true);
        
            Destroy(GameObject.FindGameObjectWithTag("Enemy"));
            SceneManager.LoadScene("The great Alex");  // Replace with the name of your next scene

        }

    }





}