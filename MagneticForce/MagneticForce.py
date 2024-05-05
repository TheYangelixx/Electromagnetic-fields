import math
import os
from PIL import Image

class MForce():
    def __init__(self, eFlow = 1, length = 1, magneticFieldIntensity = 1, angle = 1, electricCharge = 1, speed = 1, bDir = 'درون سو', iDir = 'درون سو', id = 0):
        self.eFlow = eFlow
        self.length = length
        self.angle = angle
        self.magneticFieldIntensity = magneticFieldIntensity
        self.electricCharge = electricCharge
        self.speed = speed
        self.bDir = bDir
        self.iDir = iDir
        self.id = id
    
    def wire_electromagnetic_force(self, magneticFieldIntensity, eFlow, length, angle):
        return (magneticFieldIntensity * eFlow * length * math.sin(math.radians(angle)))
    
    def particle_electromagnetic_force(self, magneticFieldIntensity, speed, electricCharge, angle):
        return (magneticFieldIntensity * speed * electricCharge * math.sin(math.radians(angle)))
    
    def whatDirection(self, bDir, iDir, id):
        bg = Image.open(os.path.join("MagneticForce", "images", "Background.png"))
        
        
        baseman = Image.open(os.path.join("MagneticForce", "images", "Baseman.png"))
        bzamin = Image.open(os.path.join("MagneticForce", "images", "Bzamin.png"))
        bsharq = Image.open(os.path.join("MagneticForce", "images", "Bsharq.png"))
        bqarb = Image.open(os.path.join("MagneticForce", "images", "Bqarb.png"))
        bdarunsu = Image.open(os.path.join("MagneticForce", "images", "Bdarunsu.png"))
        bburunsu = Image.open(os.path.join("MagneticForce", "images", "Bbrunsu.png"))

        faseman = Image.open(os.path.join("MagneticForce", "images", "Faseman.png"))
        fzamin = Image.open(os.path.join("MagneticForce", "images", "Fzamin.png"))
        fsharq = Image.open(os.path.join("MagneticForce", "images", "Fsharq.png"))
        fqarb = Image.open(os.path.join("MagneticForce", "images", "Fqarb.png"))
        fdarunsu = Image.open(os.path.join("MagneticForce", "images", "Fdarunsu.png"))
        fburunsu = Image.open(os.path.join("MagneticForce", "images", "Fburunsu.png"))

        iaseman = Image.open(os.path.join("MagneticForce", "images", "iaseman.png"))
        izamin = Image.open(os.path.join("MagneticForce", "images", "izamin.png"))
        isharq = Image.open(os.path.join("MagneticForce", "images", "isharq.png"))
        iqarb = Image.open(os.path.join("MagneticForce", "images", "iqarb.png"))
        idarunsu = Image.open(os.path.join("MagneticForce", "images", "idarunsu.png"))
        iburunsu = Image.open(os.path.join("MagneticForce", "images", "iburunsu.png"))

        vaseman = Image.open(os.path.join("MagneticForce", "images", "Vaseman.png"))
        vzamin = Image.open(os.path.join("MagneticForce", "images", "Vzamin.png"))
        vsharq = Image.open(os.path.join("MagneticForce", "images", "Vsharq.png"))
        vqarb = Image.open(os.path.join("MagneticForce", "images", "Vqarb.png"))
        vdarunsu = Image.open(os.path.join("MagneticForce", "images", "Vdarunsu.png"))
        vburunsu = Image.open(os.path.join("MagneticForce", "images", "Vburunsu.png"))

        bg = bg.convert("RGBA")
        baseman = baseman.convert("RGBA")
        bzamin = bzamin.convert("RGBA")
        bsharq = bsharq.convert("RGBA")
        bqarb = bqarb.convert("RGBA")
        bdarunsu = bdarunsu.convert("RGBA")
        bburunsu = bburunsu.convert("RGBA")

        iaseman = iaseman.convert("RGBA")
        izamin = izamin.convert("RGBA")
        isharq = isharq.convert("RGBA")
        iqarb = iqarb.convert("RGBA")
        idarunsu = idarunsu.convert("RGBA")
        iburunsu = iburunsu.convert("RGBA")

        faseman = faseman.convert("RGBA")
        fzamin = fzamin.convert("RGBA")
        fsharq = fsharq.convert("RGBA")
        fqarb = fqarb.convert("RGBA")
        fdarunsu = fdarunsu.convert("RGBA")
        fburunsu = fburunsu.convert("RGBA")

        vaseman = vaseman.convert("RGBA")
        vzamin = vzamin.convert("RGBA")
        vsharq = vsharq.convert("RGBA")
        vqarb = vqarb.convert("RGBA")
        vdarunsu = vdarunsu.convert("RGBA")
        vburunsu = vburunsu.convert("RGBA")
        
        baseman = baseman.resize(bg.size)
        bzamin = bzamin.resize(bg.size)
        bdarunsu = bdarunsu.resize(bg.size)
        bburunsu = bburunsu.resize(bg.size)
        bqarb = bqarb.resize(bg.size)
        bsharq = bsharq.resize(bg.size)

        iaseman = iaseman.resize(bg.size)
        izamin = izamin.resize(bg.size)
        idarunsu = idarunsu.resize(bg.size)
        iburunsu = iburunsu.resize(bg.size)
        iqarb = iqarb.resize(bg.size)
        isharq = isharq.resize(bg.size)

        vaseman = vaseman.resize(bg.size)
        vzamin = vzamin.resize(bg.size)
        vdarunsu = vdarunsu.resize(bg.size)
        vburunsu = vburunsu.resize(bg.size)
        vqarb = vqarb.resize(bg.size)
        vsharq = vsharq.resize(bg.size)

        faseman = faseman.resize(bg.size)
        fzamin = fzamin.resize(bg.size)
        fdarunsu = fdarunsu.resize(bg.size)
        fburunsu = fburunsu.resize(bg.size)
        fqarb = fqarb.resize(bg.size)
        fsharq = fsharq.resize(bg.size)


        if bDir == 'شرق':
            result = Image.new('RGBA', bg.size)
            result = Image.alpha_composite(result, bg)
            result = Image.alpha_composite(result, bsharq)
            if iDir == 'آسمان':
                if id == 0:
                    result = Image.alpha_composite(result, iaseman)
                else:
                    result = Image.alpha_composite(result, vaseman)
                result = Image.alpha_composite(result, fdarunsu)
                result.save('result.png')
                return ("سو درون")
            elif iDir == 'زمین':
                if id == 0:
                    result = Image.alpha_composite(result, izamin)
                else:
                    result = Image.alpha_composite(result, vzamin)
                result = Image.alpha_composite(result, fburunsu)
                result.save('result.png')
                return ("سو برون")
            elif iDir == 'درون سو':
                if id == 0:
                    result = Image.alpha_composite(result, idarunsu)
                else:
                    result = Image.alpha_composite(result, vdarunsu)
                result = Image.alpha_composite(result, fzamin)
                result.save('result.png')
                return ("زمین")
            elif iDir == 'برون سو':
                if id == 0:
                    result = Image.alpha_composite(result, iburunsu)
                else:
                    result = Image.alpha_composite(result, vburunsu)
                result = Image.alpha_composite(result, faseman)
                result.save('result.png')
                return ("آسمان")
            else:
                result = Image.new('RGBA', bg.size)
                result = Image.alpha_composite(result, bg)
                result.save('result.png')
                return ("NONE")
            

        elif bDir == 'آسمان':
            result = Image.new('RGBA', bg.size)
            result = Image.alpha_composite(result, bg)
            result = Image.alpha_composite(result, baseman)
            if iDir == 'غرب':
                if id == 0 :
                    result = Image.alpha_composite(result, iqarb)
                else:
                    result = Image.alpha_composite(result, vqarb)
                result = Image.alpha_composite(result, fdarunsu)
                result.save('result.png')
                return ("سو درون")
            elif iDir == 'شرق':
                if id == 0:
                    result = Image.alpha_composite(result, isharq)
                else:
                    result = Image.alpha_composite(result, vsharq)
                result = Image.alpha_composite(result, fburunsu)
                result.save('result.png')
                return ("سو برون")
            elif iDir == 'درون سو':
                if id == 0:
                    result = Image.alpha_composite(result, idarunsu)
                else:
                    result = Image.alpha_composite(result, vdarunsu)
                result = Image.alpha_composite(result, fsharq)
                result.save('result.png')
                return ("شرق")
            elif iDir == 'برون سو':
                if id == 0:
                    result = Image.alpha_composite(result, iburunsu)
                else:
                    result = Image.alpha_composite(result, vburunsu)
                result = Image.alpha_composite(result, fqarb)
                result.save('result.png')
                return ("غرب")
            else:
                result = Image.new('RGBA', bg.size)
                result = Image.alpha_composite(result, bg)
                result.save('result.png')
                return ("NONE")

        elif bDir == 'غرب':
            result = Image.new('RGBA', bg.size)
            result = Image.alpha_composite(result, bg)
            result = Image.alpha_composite(result, bqarb)
            if iDir == 'آسمان':
                if id == 0:
                    result = Image.alpha_composite(result, iaseman)
                else :
                    result = Image.alpha_composite(result, vaseman)
                result = Image.alpha_composite(result, fburunsu)
                result.save('result.png')
                return ("سو برون")
            elif iDir == 'زمین':
                if id == 0:
                    result = Image.alpha_composite(result, izamin)
                else:
                    result = Image.alpha_composite(result, vzamin)
                result = Image.alpha_composite(result, fdarunsu)
                result.save('result.png')
                return ("سو درون")
            elif iDir == 'درون سو':
                if id ==0 :
                    result = Image.alpha_composite(result, idarunsu)
                else:
                    result = Image.alpha_composite(result, vdarunsu)
                result = Image.alpha_composite(result, faseman)
                result.save('result.png')
                return ("آسمان")
            elif iDir == 'برون سو':
                if id == 0:
                    result = Image.alpha_composite(result, iburunsu)
                else:
                    result = Image.alpha_composite(result, vburunsu)
                result = Image.alpha_composite(result, fzamin)
                result.save('result.png')
                return ("زمین")
            else:
                result = Image.new('RGBA', bg.size)
                result = Image.alpha_composite(result, bg)
                result.save('result.png')
                return ("NONE")

        elif bDir == 'زمین':
            result = Image.new('RGBA', bg.size)
            result = Image.alpha_composite(result, bg)
            result = Image.alpha_composite(result, bzamin)
            if iDir == 'شرق':
                if id == 0:
                    result = Image.alpha_composite(result, isharq)
                else :
                    result = Image.alpha_composite(result, vsharq)
                result = Image.alpha_composite(result, fdarunsu)
                result.save('result.png')
                return ("سو درون")
            elif iDir == 'غرب':
                if id == 0:
                    result = Image.alpha_composite(result, iqarb)
                else:
                    result = Image.alpha_composite(result, vqarb)
                result = Image.alpha_composite(result, fburunsu)
                result.save('result.png')
                return ("سو برون")
            elif iDir == 'درون سو':
                if id == 0:
                    result = Image.alpha_composite(result, idarunsu)
                else:
                    result = Image.alpha_composite(result, vdarunsu)
                result = Image.alpha_composite(result, fqarb)
                result.save('result.png')
                return ("غرب")
            elif iDir == 'برون سو':
                if id ==0:
                    result = Image.alpha_composite(result, iburunsu)
                else:
                    result = Image.alpha_composite(result, vburunsu)
                result = Image.alpha_composite(result, fsharq)
                result.save('result.png')
                return ("شرق")
            else:
                result = Image.new('RGBA', bg.size)
                result = Image.alpha_composite(result, bg)
                result.save('result.png')
                return ("NONE")
            
        elif bDir == 'درون سو':
            result = Image.new('RGBA', bg.size)
            result = Image.alpha_composite(result, bg)
            result = Image.alpha_composite(result, bdarunsu)
            if iDir == 'آسمان':
                if id == 0:
                    result = Image.alpha_composite(result, iaseman)
                else:
                    result = Image.alpha_composite(result, vaseman)
                result = Image.alpha_composite(result, fqarb)
                result.save('result.png')
                return ("غرب")
            elif iDir == 'شرق':
                if id ==0:
                    result = Image.alpha_composite(result, isharq)
                else:
                    result = Image.alpha_composite(result, vsharq)
                result = Image.alpha_composite(result, faseman)
                result.save('result.png')
                return ("آسمان")
            elif iDir == 'زمین':
                if id ==0:
                    result = Image.alpha_composite(result, izamin)
                else:
                    result = Image.alpha_composite(result, vzamin)
                result = Image.alpha_composite(result, fsharq)
                result.save('result.png')
                return ("شرق")
            elif iDir == 'غرب':
                if id == 0:
                    result = Image.alpha_composite(result, iqarb)
                else:
                    result = Image.alpha_composite(result, vqarb)
                result = Image.alpha_composite(result, fzamin)
                result.save('result.png')
                return ("زمین")
            else:
                result = Image.new('RGBA', bg.size)
                result = Image.alpha_composite(result, bg)
                result.save('result.png')
                return ("NONE")

        elif bDir == 'برون سو':
            result = Image.new('RGBA', bg.size)
            result = Image.alpha_composite(result, bg)
            result = Image.alpha_composite(result, bburunsu)
            if iDir == 'غرب':
                if id == 0:
                    result = Image.alpha_composite(result, iqarb)
                else:
                    result = Image.alpha_composite(result, vqarb)
                result = Image.alpha_composite(result, faseman)
                result.save('result.png')
                return ("آسمان")
            elif iDir == 'زمین':
                if id == 0:
                    result = Image.alpha_composite(result, izamin)
                else:
                    result = Image.alpha_composite(result, vzamin)
                result = Image.alpha_composite(result, fqarb)
                result.save('result.png')
                return ("غرب")
            elif iDir == 'شرق':
                if id ==0:
                    result = Image.alpha_composite(result, isharq)
                else:
                    result = Image.alpha_composite(result, vsharq)
                result = Image.alpha_composite(result, fzamin)
                result.save('result.png')
                return ("زمین")
            elif iDir == 'آسمان':
                if id == 0:
                    result = Image.alpha_composite(result, iaseman)
                else:
                    result = Image.alpha_composite(result, vaseman)
                result = Image.alpha_composite(result, fsharq)
                result.save('result.png')
                return ("شرق")
            else:
                result = Image.new('RGBA', bg.size)
                result = Image.alpha_composite(result, bg)
                result.save('result.png')
                return ("NONE")