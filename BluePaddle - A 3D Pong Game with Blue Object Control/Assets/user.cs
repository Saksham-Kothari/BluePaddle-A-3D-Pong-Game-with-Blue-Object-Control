using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class user : MonoBehaviour
{

    float speed = 3f;
    public Transform aimTarget;
    bool hitting = false;
    float force = 100f;

    void Update()
    {
        float x = Input.GetAxisRaw("Horizontal");

        float y = Input.GetAxisRaw("Vertical");
        if (Input.GetKeyDown(KeyCode.F))
        {
            hitting = true;
        }
        else if (Input.GetKeyUp(KeyCode.F))
        {
            hitting = false;
        }
        if (hitting)
        {
            aimTarget.Translate(new Vector3(x, 0, 0) * speed * Time.deltaTime);
        }
        if ((x != 0 || y != 0) && !hitting)
        {
            transform.Translate(new Vector3(x, 0, y) * speed * Time.deltaTime);
        }
    }
    private void OnTriggerEnter(Collider other)
    {
        if(other.CompareTag("bsll"))
        {
            Vector3 dir= aimTarget.position - transform.position;
            other.GetComponent<Rigidbody>().velocity = dir.normalized*force +new Vector3(0,3,0);
        }
    }
}
